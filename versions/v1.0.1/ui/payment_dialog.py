"""
付费弹窗 - Payment Dialog v3
支持：
  - 浏览器打开支付页面（接入第三方支付API）
  - 内置收款码模式（如果没配置API）
  - 订单号验证
"""
import os
from PyQt5.QtCore import (
    Qt, QSize, QPropertyAnimation, QEasingCurve, QPoint, pyqtSignal, QTimer
)
from PyQt5.QtWidgets import (
    QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QMessageBox, QFrame, QGraphicsDropShadowEffect, QComboBox
)
from PyQt5.QtGui import QPixmap, QPainter, QColor, QIcon, QFont

from core.subscription import SubscriptionManager
from core.payment_api import PaymentAPI


class PaymentDialog(QDialog):
    """付费弹窗 - 支持浏览器支付"""

    payment_successful = pyqtSignal()

    def __init__(self, subscription_manager=None, parent=None):
        super().__init__(parent)
        self.sub = subscription_manager or SubscriptionManager()
        self.payment_api = PaymentAPI()
        self._selected_plan = 'weekly'
        self._selected_pay_type = 'wechat'
        self._current_order_id = None

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Dialog
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(480, 640)

        self._setup_ui()

    def _setup_ui(self):
        main = QWidget(self)
        main.setGeometry(0, 0, 480, 640)
        main.setStyleSheet("""
            QWidget {
                background: rgba(25, 25, 45, 0.98);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 24px;
                color: white;
            }
        """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(0, 8)
        main.setGraphicsEffect(shadow)

        layout = QVBoxLayout(main)
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(14)

        # 标题
        title_layout = QHBoxLayout()
        icon_label = QLabel("💎")
        icon_label.setStyleSheet("font-size: 28px; background: transparent; border: none;")
        title_layout.addWidget(icon_label)
        title_label = QLabel("解锁全部功能")
        title_label.setStyleSheet("font-size: 22px; font-weight: 700; color: white; background: transparent; border: none;")
        title_layout.addWidget(title_label)
        title_layout.addStretch()

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(32, 32)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet("""
            QPushButton {
                background: rgba(255,255,255,0.08);
                border: none;
                border-radius: 16px;
                color: rgba(255,255,255,0.6);
                font-size: 14px;
            }
            QPushButton:hover {
                background: rgba(255,255,255,0.15);
                color: white;
            }
        """)
        close_btn.clicked.connect(self.reject)
        title_layout.addWidget(close_btn)
        layout.addLayout(title_layout)

        # 状态
        info = self.sub.get_info()
        if info['status'] == 'trial':
            status_text = f"🎁 免费试用还剩 <b style='color:#4ade80'>{info['trial_days']}</b> 天"
        elif info['status'] == 'active':
            status_text = f"✅ 订阅有效期至 <b style='color:#4ade80'>{info['subscription_end']}</b>"
        else:
            status_text = "⏰ 免费试用已结束，请激活解锁"

        status_label = QLabel(status_text)
        status_label.setStyleSheet("font-size: 13px; color: rgba(255,255,255,0.75); background: transparent; border: none;")
        layout.addWidget(status_label)

        # 分隔线
        self._add_separator(layout)

        # 套餐选择
        plan_title = QLabel("选择套餐")
        plan_title.setStyleSheet("font-size: 13px; font-weight: 600; color: white; background: transparent; border: none;")
        layout.addWidget(plan_title)

        plans_layout = QHBoxLayout()
        plans_layout.setSpacing(8)

        self.plan_buttons = {}
        plans = self.payment_api.get_plans()
        for plan_id, plan_info in plans.items():
            btn = QPushButton()
            btn.setCheckable(True)
            btn.setFixedHeight(64)
            btn.setCursor(Qt.PointingHandCursor)

            btn_layout = QVBoxLayout(btn)
            btn_layout.setContentsMargins(8, 6, 8, 6)
            btn_layout.setSpacing(0)
            btn_layout.setAlignment(Qt.AlignCenter)

            name_label = QLabel(plan_info['name'])
            name_label.setAlignment(Qt.AlignCenter)
            name_label.setStyleSheet("font-size: 12px; color: rgba(255,255,255,0.7); background: transparent;")
            btn_layout.addWidget(name_label)

            price_layout = QHBoxLayout()
            price_layout.setAlignment(Qt.AlignCenter)
            price_label = QLabel(f"¥{plan_info['price']:.0f}")
            price_label.setStyleSheet("font-size: 18px; font-weight: 700; color: white; background: transparent;")
            unit_label = QLabel("/" + plan_info['description'].split('使')[0])
            unit_label.setStyleSheet("font-size: 11px; color: rgba(255,255,255,0.5); background: transparent;")
            price_layout.addWidget(price_label)
            price_layout.addWidget(unit_label)
            btn_layout.addLayout(price_layout)

            self._set_plan_style(btn, selected=(plan_id == 'weekly'))
            btn.clicked.connect(lambda _, p=plan_id: self._select_plan(p))
            self.plan_buttons[plan_id] = btn
            plans_layout.addWidget(btn)

        layout.addLayout(plans_layout)

        # 分隔线
        self._add_separator(layout)

        # 支付方式
        pay_title = QLabel("支付方式")
        pay_title.setStyleSheet("font-size: 13px; font-weight: 600; color: white; background: transparent; border: none;")
        layout.addWidget(pay_title)

        pay_types_layout = QHBoxLayout()
        pay_types_layout.setSpacing(8)

        self.pay_type_buttons = {}
        pay_types = self.payment_api.get_payment_types()
        for pt_id, pt_name in pay_types.items():
            btn = QPushButton(pt_name)
            btn.setCheckable(True)
            btn.setFixedHeight(40)
            btn.setCursor(Qt.PointingHandCursor)
            self._set_pay_type_style(btn, selected=(pt_id == 'wechat'))
            btn.clicked.connect(lambda _, p=pt_id: self._select_pay_type(p))
            self.pay_type_buttons[pt_id] = btn
            pay_types_layout.addWidget(btn)

        layout.addLayout(pay_types_layout)

        # 分隔线
        self._add_separator(layout)

        # 支付区域
        self._setup_pay_area(layout)

        # 订单号验证
        verify_layout = QVBoxLayout()
        verify_layout.setSpacing(6)

        verify_label = QLabel("支付完成后，输入订单号：")
        verify_label.setStyleSheet("font-size: 12.5px; color: rgba(255,255,255,0.65); background: transparent;")
        verify_layout.addWidget(verify_label)

        self.order_input = QLineEdit()
        self.order_input.setPlaceholderText("请输入订单号（选填，信任模式可直接点激活）")
        self.order_input.setFixedHeight(40)
        self.order_input.setStyleSheet("""
            QLineEdit {
                background: rgba(0,0,0,0.3);
                border: 1.5px solid rgba(255,255,255,0.1);
                border-radius: 9px;
                padding: 0 14px;
                color: white;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 1.5px solid rgba(100, 150, 255, 0.6);
            }
        """)
        verify_layout.addWidget(self.order_input)

        layout.addLayout(verify_layout)

        # 激活按钮
        activate_btn = QPushButton("✅  我已支付，立即激活")
        activate_btn.setFixedHeight(46)
        activate_btn.setCursor(Qt.PointingHandCursor)
        activate_btn.setStyleSheet("""
            QPushButton {
                background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
                border: none;
                border-radius: 12px;
                color: white;
                font-size: 15px;
                font-weight: 700;
            }
            QPushButton:hover {
                background: linear-gradient(135deg, #6ee7a8 0%, #34d970 100%);
            }
            QPushButton:pressed {
                background: linear-gradient(135deg, #3cc96a 0%, #1bb04c 100%);
            }
        """)
        activate_btn.clicked.connect(self._on_activate)
        self.order_input.returnPressed.connect(self._on_activate)
        layout.addWidget(activate_btn)

        # 底部
        bottom_hint = QLabel("🔒 支付安全 · 由您配置的支付平台提供服务")
        bottom_hint.setAlignment(Qt.AlignCenter)
        bottom_hint.setStyleSheet("font-size: 11px; color: rgba(255,255,255,0.3); background: transparent;")
        layout.addWidget(bottom_hint)

        # 自动创建订单
        QTimer.singleShot(200, self._create_order)

    def _add_separator(self, layout):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background: rgba(255,255,255,0.08); border: none; max-height: 1px;")
        layout.addWidget(line)

    def _setup_pay_area(self, layout):
        """设置支付区域"""
        # 收款码容器
        qr_container = QWidget()
        qr_container.setFixedHeight(160)
        qr_container.setStyleSheet("""
            QWidget {
                background: rgba(255,255,255,0.04);
                border: 2px solid rgba(255,255,255,0.08);
                border-radius: 14px;
            }
        """)

        qr_layout = QVBoxLayout(qr_container)
        qr_layout.setAlignment(Qt.AlignCenter)
        qr_layout.setSpacing(6)

        self.qr_image_label = QLabel()
        self.qr_image_label.setAlignment(Qt.AlignCenter)
        self.qr_image_label.setFixedSize(110, 110)
        self.qr_image_label.setStyleSheet("background: transparent;")
        qr_layout.addWidget(self.qr_image_label)

        self.qr_hint = QLabel("")
        self.qr_hint.setAlignment(Qt.AlignCenter)
        self.qr_hint.setStyleSheet("font-size: 12.5px; color: rgba(255,255,255,0.6); background: transparent;")
        qr_layout.addWidget(self.qr_hint)

        self.qr_amount = QLabel("")
        self.qr_amount.setAlignment(Qt.AlignCenter)
        self.qr_amount.setStyleSheet("font-size: 14px; color: #4ade80; font-weight: 700; background: transparent;")
        qr_layout.addWidget(self.qr_amount)

        # 打开浏览器支付按钮
        self.browser_btn = QPushButton("🌐  在浏览器中打开支付页面")
        self.browser_btn.setFixedHeight(40)
        self.browser_btn.setCursor(Qt.PointingHandCursor)
        self.browser_btn.setStyleSheet("""
            QPushButton {
                background: rgba(59, 130, 246, 0.25);
                border: 1.5px solid rgba(59, 130, 246, 0.5);
                border-radius: 10px;
                color: white;
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: rgba(59, 130, 246, 0.4);
            }
        """)
        self.browser_btn.clicked.connect(self._open_browser_pay)

        qr_layout.addWidget(self.browser_btn)

        layout.addWidget(qr_container)

        # 加载内容
        QTimer.singleShot(300, self._update_pay_area)

    def _set_plan_style(self, btn, selected=False):
        if selected:
            btn.setStyleSheet("""
                QPushButton {
                    background: rgba(100, 150, 255, 0.25);
                    border: 2px solid rgba(100, 150, 255, 0.7);
                    border-radius: 10px;
                }
                QPushButton:checked {
                    background: rgba(100, 150, 255, 0.3);
                    border: 2px solid rgba(100, 150, 255, 0.85);
                }
            """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    background: rgba(255,255,255,0.04);
                    border: 1.5px solid rgba(255,255,255,0.08);
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background: rgba(255,255,255,0.08);
                    border: 1.5px solid rgba(255,255,255,0.18);
                }
                QPushButton:checked {
                    background: rgba(100, 150, 255, 0.2);
                    border: 2px solid rgba(100, 150, 255, 0.6);
                }
            """)

    def _set_pay_type_style(self, btn, selected=False):
        if selected:
            btn.setStyleSheet("""
                QPushButton {
                    background: rgba(34, 197, 94, 0.25);
                    border: 2px solid rgba(34, 197, 94, 0.7);
                    border-radius: 10px;
                    color: white;
                    font-size: 13px;
                    font-weight: 600;
                }
                QPushButton:checked {
                    background: rgba(34, 197, 94, 0.3);
                    border: 2px solid rgba(34, 197, 94, 0.85);
                }
            """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    background: rgba(255,255,255,0.04);
                    border: 1.5px solid rgba(255,255,255,0.08);
                    border-radius: 10px;
                    color: white;
                    font-size: 13px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background: rgba(255,255,255,0.08);
                    border: 1.5px solid rgba(255,255,255,0.18);
                }
                QPushButton:checked {
                    background: rgba(34, 197, 94, 0.25);
                    border: 2px solid rgba(34, 197, 94, 0.7);
                }
            """)

    def _select_plan(self, plan_id):
        self._selected_plan = plan_id
        for pid, btn in self.plan_buttons.items():
            btn.setChecked(pid == plan_id)
            self._set_plan_style(btn, selected=(pid == plan_id))
        self._create_order()

    def _select_pay_type(self, pay_type):
        self._selected_pay_type = pay_type
        for pt, btn in self.pay_type_buttons.items():
            btn.setChecked(pt == pay_type)
            self._set_pay_type_style(btn, selected=(pt == pay_type))
        self._create_order()

    def _create_order(self):
        """创建订单"""
        order_id, pay_url, error = self.payment_api.create_order(
            self._selected_plan, self._selected_pay_type
        )
        if order_id:
            self._current_order_id = order_id
            self.order_input.setText(order_id)
            self._update_pay_area(pay_url)

    def _update_pay_area(self, pay_url=None):
        """更新支付区域显示"""
        plans = self.payment_api.get_plans()
        plan = plans.get(self._selected_plan, {})
        price = plan.get('price', 3)

        has_api = self.payment_api.is_configured()

        if has_api and pay_url:
            # 配置了API，显示浏览器支付
            self.qr_hint.setText("点击下方按钮在浏览器中完成支付")
            self.qr_amount.setText(f"请支付 ¥{price:.0f}")
            self.qr_image_label.setText("🌐")
            self.qr_image_label.setStyleSheet("font-size: 48px; background: transparent;")
            self.browser_btn.show()
        else:
            # 没配置API，尝试显示本地收款码
            self.browser_btn.hide()
            config_dir = os.path.join(os.path.expanduser('~'), '.nexus_dock')
            qr_path = None
            for name in ['wechat_qr.png', 'wechat.png', '微信收款码.png', 'qr.png', 'qrcode.png']:
                p = os.path.join(config_dir, name)
                if os.path.exists(p):
                    qr_path = p
                    break

            if qr_path:
                pixmap = QPixmap(qr_path)
                if not pixmap.isNull():
                    scaled = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    self.qr_image_label.setPixmap(scaled)
                    self.qr_hint.setText("请扫码支付")
                    self.qr_amount.setText(f"请支付 ¥{price:.0f}")
                    return

            # 没有收款码
            self.qr_image_label.setText("📱")
            self.qr_image_label.setStyleSheet("font-size: 48px; background: transparent;")
            self.qr_hint.setText("请在浏览器中完成支付")
            self.qr_amount.setText(f"请支付 ¥{price:.0f}")
            self.browser_btn.show()

    def _open_browser_pay(self):
        """在浏览器中打开支付页面"""
        if self._current_order_id:
            self.payment_api.open_browser_pay(self._current_order_id)
        else:
            self._create_order()
            if self._current_order_id:
                self.payment_api.open_browser_pay(self._current_order_id)

    def _on_activate(self):
        """激活"""
        order_id = self.order_input.text().strip()

        if not order_id:
            reply = QMessageBox.question(
                self, "确认激活",
                "还没有输入订单号，确认已经付款了吗？\n\n"
                "（信任模式：如果您确认已付款，可以直接激活）",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply != QMessageBox.Yes:
                return

        # 如果有订单号，尝试验证
        if order_id:
            verified, msg = self.payment_api.verify_order(order_id)
            if not verified and order_id != self._current_order_id:
                # 验证失败但可能是信任模式，询问
                reply = QMessageBox.question(
                    self, "验证",
                    f"订单验证结果：{msg}\n\n"
                    f"是否仍然激活？（确认已付款可选是）",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )
                if reply != QMessageBox.Yes:
                    return

        # 手动标记订单为已支付
        if self._current_order_id:
            self.payment_api.mark_paid_manually(self._current_order_id)

        # 激活订阅
        plans = self.payment_api.get_plans()
        plan = plans.get(self._selected_plan, {})
        weeks = plan.get('weeks', 1)
        self.sub.activate_subscription(weeks)

        QMessageBox.information(
            self, "激活成功",
            f"🎉 订阅激活成功！\n\n"
            f"套餐：{plan.get('name', '周卡')}\n"
            f"有效期：+{weeks} 周\n\n"
            f"感谢您的支持！"
        )
        self.payment_successful.emit()
        self.accept()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.transparent)
