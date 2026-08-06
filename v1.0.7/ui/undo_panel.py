"""
撤销面板 - Undo Panel
显示最近的文件整理记录，支持一键撤销
"""
import os
import sys
from PyQt5.QtCore import (
    Qt, QPoint, QSize, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QTimer
)
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QListWidgetItem, QFrame, QMessageBox
)
from PyQt5.QtGui import (
    QPainter, QColor, QIcon, QPixmap, QFont, QCursor, QLinearGradient, QBrush, QPen
)


class UndoButton(QPushButton):
    """Dock栏上的撤销按钮（带小红点）"""

    undo_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.has_undo = False
        self.record_count = 0

        self.setFixedSize(56, 56)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("background: transparent; border: none;")
        self.setProperty("baseSize", QSize(56, 56))
        self.setToolTip("撤销最近的整理操作")

        self.clicked.connect(self.undo_clicked.emit)

    def set_record_count(self, count):
        self.record_count = count
        self.has_undo = count > 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()

        # 按钮背景
        gradient = QLinearGradient(0, 0, 0, rect.height())
        gradient.setColorAt(0, QColor(100, 100, 120, 180))
        gradient.setColorAt(1, QColor(60, 60, 80, 200))

        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(QColor(255, 255, 255, 30), 1))
        painter.drawRoundedRect(4, 4, rect.width() - 8, rect.height() - 8, 12, 12)

        # 撤销图标（↩箭头）
        painter.setPen(QColor(255, 255, 255, 230))
        font = painter.font()
        font.setPointSize(20)
        painter.setFont(font)
        painter.drawText(rect, Qt.AlignCenter, "↩")

        # 小红点提示
        if self.has_undo:
            dot_rect = QRect(rect.width() - 16, 4, 12, 12)
            painter.setBrush(QColor(255, 80, 80, 240))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(dot_rect)

            # 数量角标
            if self.record_count > 1:
                badge_text = str(self.record_count) if self.record_count < 10 else "9+"
                painter.setPen(QColor(255, 255, 255))
                font = painter.font()
                font.setPointSize(8)
                font.setBold(True)
                painter.setFont(font)
                painter.drawText(dot_rect, Qt.AlignCenter, badge_text)


class UndoRecordItem(QWidget):
    """撤销记录列表项"""

    undo_requested = pyqtSignal(int)

    def __init__(self, record, parent=None):
        super().__init__(parent)
        self.record = record
        self.record_id = record.get('id')
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(10)

        # 图标
        icon_text = "📦" if self.record.get('is_batch') else "📁"
        icon_label = QLabel(icon_text)
        icon_label.setStyleSheet("font-size: 18px; background: transparent;")
        icon_label.setFixedWidth(28)
        layout.addWidget(icon_label)

        # 信息
        info_layout = QVBoxLayout()
        info_layout.setSpacing(2)

        is_batch = self.record.get('is_batch')
        if is_batch:
            count = self.record.get('batch_count', 0)
            title = f"一键整理 · {count} 个文件"
        else:
            title = f"{self.record.get('filename', '未知')}"

        title_label = QLabel(title)
        title_label.setStyleSheet("color: white; font-size: 13px; font-weight: 500; background: transparent;")
        title_label.setWordWrap(True)
        info_layout.addWidget(title_label)

        time_label = QLabel(self.record.get('datetime', ''))
        time_label.setStyleSheet("color: rgba(255,255,255,0.4); font-size: 11px; background: transparent;")
        info_layout.addWidget(time_label)

        layout.addLayout(info_layout, 1)

        # 撤销按钮
        undo_btn = QPushButton("撤销")
        undo_btn.setFixedSize(56, 28)
        undo_btn.setCursor(Qt.PointingHandCursor)
        undo_btn.setStyleSheet("""
            QPushButton {
                background: rgba(255, 100, 100, 0.2);
                border: 1px solid rgba(255, 100, 100, 0.4);
                border-radius: 6px;
                color: rgb(255, 180, 180);
                font-size: 12px;
                font-weight: 500;
            }
            QPushButton:hover {
                background: rgba(255, 100, 100, 0.35);
                color: white;
            }
        """)
        undo_btn.clicked.connect(lambda: self.undo_requested.emit(self.record_id))
        layout.addWidget(undo_btn)


class UndoPanel(QWidget):
    """撤销面板 - 显示最近10次整理记录"""

    undo_performed = pyqtSignal(int, int)  # (恢复数, 跳过数)

    def __init__(self, undo_manager=None, parent=None):
        super().__init__(parent)
        self.undo_manager = undo_manager

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Popup |
            Qt.NoDropShadowWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedWidth(400)

        self._setup_ui()

    def _setup_ui(self):
        # 背景容器
        container = QWidget(self)
        container.setStyleSheet("""
            QWidget {
                background: rgba(25, 25, 45, 0.95);
                backdrop-filter: blur(30px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 18px;
            }
        """)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # 标题栏
        header = QHBoxLayout()
        icon_label = QLabel("↩")
        icon_label.setStyleSheet("font-size: 22px; background: transparent; border: none;")
        header.addWidget(icon_label)

        title_label = QLabel("撤销最近的整理")
        title_label.setStyleSheet("font-size: 17px; font-weight: 700; color: white; background: transparent; border: none;")
        header.addWidget(title_label)
        header.addStretch()

        self.count_label = QLabel("0 条记录")
        self.count_label.setStyleSheet("font-size: 12px; color: rgba(255,255,255,0.5); background: transparent; border: none;")
        header.addWidget(self.count_label)

        layout.addLayout(header)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background: rgba(255,255,255,0.08); border: none; max-height: 1px;")
        layout.addWidget(line)

        # 记录列表
        self.record_list = QListWidget()
        self.record_list.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                outline: none;
            }
            QListWidget::item {
                background: transparent;
                padding: 0;
                margin: 2px 0;
            }
        """)
        layout.addWidget(self.record_list, 1)

        # 空状态
        self.empty_label = QLabel("暂无撤销记录\n整理桌面或监控到新文件后会出现在这里")
        self.empty_label.setAlignment(Qt.AlignCenter)
        self.empty_label.setStyleSheet("color: rgba(255,255,255,0.3); font-size: 12px; padding: 30px; background: transparent;")
        self.record_list.setEmptyLabel = False
        layout.addWidget(self.empty_label)

        # 底部提示
        tip_label = QLabel("💡 最多保留最近 10 次操作记录")
        tip_label.setStyleSheet("color: rgba(255,255,255,0.3); font-size: 11px; background: transparent;")
        tip_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(tip_label)

        container.setGeometry(0, 0, 400, 420)
        self.setFixedHeight(420)

    def show_panel(self, pos):
        """显示撤销面板"""
        self._load_records()
        self.move(pos.x() - 400 // 2, pos.y() - 420 - 10)
        self.show()

    def _load_records(self):
        """加载撤销记录"""
        self.record_list.clear()

        if not self.undo_manager:
            self.empty_label.show()
            return

        records = self.undo_manager.get_records()
        self.count_label.setText(f"{len(records)} 条记录")

        if not records:
            self.empty_label.show()
            return

        self.empty_label.hide()

        for record in records:
            item = QListWidgetItem(self.record_list)
            record_widget = UndoRecordItem(record)
            record_widget.undo_requested.connect(self._on_undo_requested)
            item.setSizeHint(record_widget.sizeHint())
            self.record_list.addItem(item)
            self.record_list.setItemWidget(item, record_widget)

    def _on_undo_requested(self, record_id):
        """执行撤销"""
        if not self.undo_manager:
            return

        reply = QMessageBox.question(
            self, "确认撤销",
            "确定要撤销这次整理吗？\n文件将被移回原来的位置。",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            restored, skipped = self.undo_manager.undo_record(record_id)
            self.undo_performed.emit(restored, skipped)
            self.close()

            if restored > 0:
                QMessageBox.information(
                    self, "撤销成功",
                    f"✅ 已成功撤销！\n恢复了 {restored} 个文件"
                    + (f"\n跳过 {skipped} 个文件（文件不存在）" if skipped > 0 else "")
                )
            else:
                QMessageBox.warning(
                    self, "撤销失败",
                    "没有找到可以恢复的文件，可能文件已被移动或删除。"
                )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.transparent)
