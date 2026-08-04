#!/usr/bin/env python3
"""
激活码生成器（卖家版）
用于生成和管理 TidyUUUUp 的激活码
带图形界面，使用简单
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QComboBox, QSpinBox, QTableWidget, QTableWidgetItem,
    QHeaderView, QMessageBox, QFileDialog, QTabWidget, QTextEdit, QFrame
)
from PyQt5.QtGui import QIcon, QColor, QPainter, QPixmap, QFont

from core.activation import ActivationCodeManager


def create_icon():
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    from PyQt5.QtGui import QLinearGradient
    gradient = QLinearGradient(0, 0, 64, 64)
    gradient.setColorAt(0, QColor(74, 222, 128))
    gradient.setColorAt(1, QColor(34, 197, 94))
    painter.setBrush(gradient)
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(4, 4, 56, 56, 16, 16)
    painter.setPen(QColor(255, 255, 255, 230))
    font = QFont()
    font.setBold(True)
    font.setPointSize(28)
    painter.setFont(font)
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "🎫")
    painter.end()
    return QIcon(pixmap)


class CodeGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = ActivationCodeManager()
        self.setWindowTitle("🎫 激活码生成器 - TidyUUUUp 卖家版")
        self.setMinimumSize(700, 550)
        self._setup_ui()
        self._refresh_table()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        # 标题
        title_layout = QHBoxLayout()
        title = QLabel("🎫  TidyUUUUp 激活码生成器")
        title.setStyleSheet("font-size: 22px; font-weight: 700; color: #22c55e;")
        title_layout.addWidget(title)
        title_layout.addStretch()
        layout.addLayout(title_layout)

        # 标签页
        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid rgba(0,0,0,0.1);
                border-radius: 12px;
                background: white;
            }
            QTabBar::tab {
                background: #f0f0f0;
                border: none;
                padding: 10px 24px;
                margin: 4px;
                border-radius: 8px;
                font-size: 13px;
                font-weight: 500;
            }
            QTabBar::tab:selected {
                background: #22c55e;
                color: white;
            }
        """)

        # 标签1：生成激活码
        generate_tab = QWidget()
        generate_layout = QVBoxLayout(generate_tab)
        generate_layout.setContentsMargins(20, 20, 20, 20)
        generate_layout.setSpacing(14)

        # 生成设置
        settings_card = QFrame()
        settings_card.setStyleSheet("background: #f8fafc; border-radius: 12px; padding: 16px;")
        settings_layout = QVBoxLayout(settings_card)
        settings_layout.setSpacing(12)

        # 数量
        count_layout = QHBoxLayout()
        count_label = QLabel("生成数量:")
        count_label.setStyleSheet("font-size: 13px; font-weight: 500; color: #333;")
        count_layout.addWidget(count_label)
        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 1000)
        self.count_spin.setValue(10)
        self.count_spin.setStyleSheet("padding: 6px 12px; border: 1px solid #ddd; border-radius: 6px;")
        count_layout.addWidget(self.count_spin)
        count_layout.addStretch()
        settings_layout.addLayout(count_layout)

        # 套餐
        plan_layout = QHBoxLayout()
        plan_label = QLabel("订阅套餐:")
        plan_label.setStyleSheet("font-size: 13px; font-weight: 500; color: #333;")
        plan_layout.addWidget(plan_label)
        self.plan_combo = QComboBox()
        self.plan_combo.addItems([
            "周卡 - 1周 (3元)",
            "月卡 - 4周 (10元)",
            "年卡 - 52周 (88元)",
        ])
        self.plan_combo.setStyleSheet("padding: 6px 12px; border: 1px solid #ddd; border-radius: 6px;")
        plan_layout.addWidget(self.plan_combo)
        plan_layout.addStretch()
        settings_layout.addLayout(plan_layout)

        # 备注
        note_layout = QHBoxLayout()
        note_label = QLabel("备注信息:")
        note_label.setStyleSheet("font-size: 13px; font-weight: 500; color: #333;")
        note_layout.addWidget(note_label)
        self.note_input = QLineEdit()
        self.note_input.setPlaceholderText("例如：买家微信名、订单号等（可选）")
        self.note_input.setStyleSheet("padding: 8px 12px; border: 1px solid #ddd; border-radius: 6px;")
        note_layout.addWidget(self.note_input)
        settings_layout.addLayout(note_layout)

        generate_layout.addWidget(settings_card)

        # 生成按钮
        generate_btn = QPushButton("✨  生成激活码")
        generate_btn.setFixedHeight(48)
        generate_btn.setCursor(Qt.PointingHandCursor)
        generate_btn.setStyleSheet("""
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
        generate_btn.clicked.connect(self._generate_codes)
        generate_layout.addWidget(generate_btn)

        # 生成结果显示
        result_label = QLabel("生成结果:")
        result_label.setStyleSheet("font-size: 13px; font-weight: 600; color: #333;")
        generate_layout.addWidget(result_label)

        self.result_text = QTextEdit()
        self.result_text.setPlaceholderText("生成的激活码会显示在这里...")
        self.result_text.setStyleSheet("""
            QTextEdit {
                background: #1e1e2e;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 12px;
                color: #4ade80;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 13px;
            }
        """)
        generate_layout.addWidget(self.result_text, 1)

        # 复制按钮
        copy_btn = QPushButton("📋  复制全部激活码")
        copy_btn.setFixedHeight(40)
        copy_btn.setCursor(Qt.PointingHandCursor)
        copy_btn.setStyleSheet("""
            QPushButton {
                background: #3b82f6;
                border: none;
                border-radius: 10px;
                color: white;
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton:hover { background: #60a5fa; }
        """)
        copy_btn.clicked.connect(self._copy_results)
        generate_layout.addWidget(copy_btn)

        tabs.addTab(generate_tab, "✨ 生成激活码")

        # 标签2：查看所有激活码
        list_tab = QWidget()
        list_layout = QVBoxLayout(list_tab)
        list_layout.setContentsMargins(20, 20, 20, 20)
        list_layout.setSpacing(12)

        # 工具栏
        toolbar = QHBoxLayout()
        self.show_unused_only = QPushButton("📋 只显示未使用")
        self.show_unused_only.setCheckable(True)
        self.show_unused_only.setStyleSheet("""
            QPushButton {
                background: #f0f0f0;
                border: none;
                padding: 8px 16px;
                border-radius: 8px;
                font-size: 12px;
            }
            QPushButton:checked {
                background: #3b82f6;
                color: white;
            }
        """)
        self.show_unused_only.clicked.connect(self._refresh_table)
        toolbar.addWidget(self.show_unused_only)

        refresh_btn = QPushButton("🔄 刷新")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background: #f0f0f0;
                border: none;
                padding: 8px 16px;
                border-radius: 8px;
                font-size: 12px;
            }
            QPushButton:hover { background: #e0e0e0; }
        """)
        refresh_btn.clicked.connect(self._refresh_table)
        toolbar.addWidget(refresh_btn)
        toolbar.addStretch()

        export_btn = QPushButton("📤 导出未使用的激活码")
        export_btn.setStyleSheet("""
            QPushButton {
                background: #8b5cf6;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 8px;
                font-size: 12px;
                font-weight: 500;
            }
            QPushButton:hover { background: #a78bfa; }
        """)
        export_btn.clicked.connect(self._export_codes)
        toolbar.addWidget(export_btn)

        list_layout.addLayout(toolbar)

        # 表格
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["激活码", "套餐", "周数", "状态", "生成时间", "备注"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.setStyleSheet("""
            QTableWidget {
                gridline-color: #eee;
                border: 1px solid #ddd;
                border-radius: 8px;
            }
            QHeaderView::section {
                background: #f8fafc;
                padding: 8px;
                border: none;
                border-bottom: 1px solid #ddd;
                font-weight: 600;
                font-size: 12px;
            }
            QTableWidget::item { padding: 6px; font-size: 12px; }
        """)
        list_layout.addWidget(self.table, 1)

        # 统计信息
        self.stats_label = QLabel("")
        self.stats_label.setStyleSheet("font-size: 12px; color: #666;")
        list_layout.addWidget(self.stats_label)

        tabs.addTab(list_tab, "📋 查看/管理")

        layout.addWidget(tabs, 1)

    def _generate_codes(self):
        count = self.count_spin.value()
        plan_map = {0: 'weekly', 1: 'monthly', 2: 'yearly'}
        plan = plan_map[self.plan_combo.currentIndex()]
        note = self.note_input.text().strip()

        codes = self.manager.batch_generate(count, plan, note)

        # 显示结果
        result_text = f"✅ 成功生成 {len(codes)} 个激活码\n"
        result_text += f"套餐: {self.plan_combo.currentText()}\n"
        if note:
            result_text += f"备注: {note}\n"
        result_text += "=" * 50 + "\n\n"

        for i, code in enumerate(codes, 1):
            result_text += f"{i:3d}. {code}\n"

        result_text += f"\n{'=' * 50}\n"
        result_text += f"💡 提示：激活码已保存到本地，可在「查看/管理」标签中查看"

        self.result_text.setText(result_text)
        self._refresh_table()

    def _refresh_table(self):
        only_unused = self.show_unused_only.isChecked()
        codes = self.manager.list_codes(only_unused=only_unused)

        self.table.setRowCount(len(codes))

        plan_names = {
            'weekly': '周卡',
            'monthly': '月卡',
            'yearly': '年卡',
            'lifetime': '永久',
        }

        for row, code_data in enumerate(codes):
            # 激活码
            item_code = QTableWidgetItem(code_data['code'])
            item_code.setFont(QFont("Consolas", 10))
            self.table.setItem(row, 0, item_code)

            # 套餐
            self.table.setItem(row, 1, QTableWidgetItem(plan_names.get(code_data['plan'], code_data['plan'])))

            # 周数
            self.table.setItem(row, 2, QTableWidgetItem(str(code_data['weeks'])))

            # 状态
            status_text = "✅ 未使用" if not code_data['used'] else f"❌ 已使用 ({code_data['used_at']})"
            status_item = QTableWidgetItem(status_text)
            if not code_data['used']:
                status_item.setForeground(QColor(34, 197, 94))
            else:
                status_item.setForeground(QColor(239, 68, 68))
            self.table.setItem(row, 3, status_item)

            # 生成时间
            self.table.setItem(row, 4, QTableWidgetItem(code_data['created']))

            # 备注
            self.table.setItem(row, 5, QTableWidgetItem(code_data['note']))

        # 统计
        all_codes = self.manager.list_codes()
        unused = sum(1 for c in all_codes if not c['used'])
        self.stats_label.setText(f"总计: {len(all_codes)} 个 | 未使用: {unused} 个 | 已使用: {len(all_codes) - unused} 个")

    def _copy_results(self):
        text = self.result_text.toPlainText()
        if text:
            # 只复制激活码部分
            lines = text.split('\n')
            codes = []
            for line in lines:
                if 'NEXUS-' in line:
                    code = line.split('NEXUS-')[-1].strip()
                    codes.append('NEXUS-' + code)
            if codes:
                QApplication.clipboard().setText('\n'.join(codes))
                QMessageBox.information(self, "已复制", f"已复制 {len(codes)} 个激活码到剪贴板！")
            else:
                QApplication.clipboard().setText(text)

    def _export_codes(self):
        filepath = self.manager.export_codes()
        QMessageBox.information(self, "导出成功", f"已导出到:\n{filepath}")


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = CodeGeneratorApp()
    window.setWindowIcon(create_icon())
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
