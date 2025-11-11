#!/usr/bin/python3

'''
七、实战案例：开发一个完整的计算器应用
结合前面的知识点，开发一个简易计算器应用，支持加减乘除四则运算，整合组件、布局、事件处理等核心功能。

7.1 功能需求
支持 0-9 数字输入；
支持加减乘除四则运算；
支持小数点和正负号；
支持清空和删除功能；
支持计算结果显示。
7.2 代码实现
'''
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QGridLayout, QPushButton
from PyQt6.QtCore import Qt
import sys
 
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my简单计算器")
        self.resize(300, 400)
        self.setFixedSize(300, 400)  # 禁止调整大小
 
        # 初始化计算状态
        self.current_text = ""  # 当前输入文本
        self.result = 0  # 计算结果
        self.operator = ""  # 运算符
        self.reset_display = False  # 是否重置显示
 
        # 设置中心组件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
 
        # 创建布局
        self.layout = QGridLayout(central_widget)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(10, 10, 10, 10)
 
        # 创建显示框
        self.create_display()
 
        # 创建按钮
        self.create_buttons()
 
    def create_display(self):
        # 显示框（只读）
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            QLineEdit {
                font-size: 24px;
                padding: 10px;
                text-align: right;
                background-color: #000;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-weight:bold;
            }
        """)
        self.display.setText("0")
        # 显示框占第一行，跨4列
        self.layout.addWidget(self.display, 0, 0, 1, 4)
 
    def create_buttons(self):
        # 按钮布局（5行4列）
        buttons = [
            ["AC", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "←", "="]
        ]
 
        # 按钮样式
        btn_style = """
            QPushButton {
                font-size: 18px;
                padding: 15px;
                border: none;
                border-radius: 4px;
                background-color: #555;
            }
            QPushButton:hover {
                background-color: #888;
            }
        """
 
        # 运算符按钮样式
        op_btn_style = btn_style + "background-color: #ff9500; color: white;"
        # 数字按钮样式
        num_btn_style = btn_style + "background-color: #f2f2f2;"
        # 等号按钮样式
        eq_btn_style = btn_style + "background-color: #ff5722; color: white;"
 
        # 添加按钮到布局
        for row in range(len(buttons)):
            for col in range(len(buttons[row])):
                btn_text = buttons[row][col]
                btn = QPushButton(btn_text)
 
                # 设置按钮样式
                if btn_text in ["+", "-", "×", "÷"]:
                    btn.setStyleSheet(op_btn_style)
                elif btn_text == "=":
                    btn.setStyleSheet(eq_btn_style)
                else:
                    btn.setStyleSheet(num_btn_style)
 
                # 绑定点击事件
                btn.clicked.connect(lambda checked, text=btn_text: self.on_button_click(text))
 
                # 添加到布局
                self.layout.addWidget(btn, row+1, col)  # 行从1开始（第0行是显示框）
 
    def on_button_click(self, text):
        if text == "AC":
            # 清空
            self.current_text = ""
            self.result = 0
            self.operator = ""
            self.display.setText("0")
        elif text == "±":
            # 正负号
            # 正负号：0 永远保持无符号
            if self.current_text == '' or self.current_text == "0":
                self.current_text = "0"
            elif self.current_text.startswith("-"):
                self.current_text = self.current_text[1:]
            else:
                self.current_text = "-" + self.current_text
            self.display.setText(self.current_text)
        elif text == "%":
            # 百分比
            if self.current_text:
                value = float(self.current_text) / 100
                self.current_text = str(value)
                self.display.setText(self.current_text)
        elif text == "←":
            # 删除
            self.current_text = self.current_text[:-1]
            self.display.setText(self.current_text if self.current_text else "0")
        elif text in ["+", "-", "×", "÷"]:
            # 运算符
            if self.current_text:
                self.result = float(self.current_text)
                self.operator = text
                self.current_text = ""
                self.reset_display = True
        elif text == "=":
            # 计算结果
            if self.current_text and self.operator:
                current_value = float(self.current_text)
                if self.operator == "+":
                    self.result += current_value
                elif self.operator == "-":
                    self.result -= current_value
                elif self.operator == "×":
                    self.result *= current_value
                elif self.operator == "÷":
                    if current_value != 0:
                        self.result /= current_value
                    else:
                        self.display.setText("错误")
                        return
                # 结果转为字符串，去除末尾的.0
                self.current_text = str(int(self.result)) if self.result.is_integer() else str(self.result)
                self.display.setText(self.current_text)
                self.operator = ""
                self.reset_display = True
        elif text == ".":
            # 小数点
            if "." not in self.current_text:
                self.current_text += "."
                self.display.setText(self.current_text)
        else:
            # 数字
            if self.reset_display:
                self.current_text = text
                self.reset_display = False
            else:
                self.current_text += text
            self.display.setText(self.current_text)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())