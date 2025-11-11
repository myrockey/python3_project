#!/usr/bin/python3

'''
6.1 菜单与工具栏：应用功能导航
菜单和工具栏是桌面应用的标准组件，用于组织核心功能（如文件操作、编辑功能）。

示例：带菜单和工具栏的主窗口
'''
def test1():
    from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox
    from PyQt6.QtGui import QIcon,QAction
    import sys,os
    
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("菜单与工具栏示例")
            self.resize(600, 400)
            self.exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
            # 设置中心组件（文本编辑区）
            self.text_edit = QTextEdit()
            self.setCentralWidget(self.text_edit)
    
            # 创建菜单
            self.create_menu()
    
            # 创建工具栏
            self.create_toolbar()
    
        def create_menu(self):
            # 获取主菜单栏
            menu_bar = self.menuBar()
    
            # 文件菜单
            file_menu = menu_bar.addMenu("文件")
    
            # 新建动作
            new_action = QAction(QIcon(self.exec_path + "/icon.jpg"), "新建", self)
            new_action.setShortcut("Ctrl+N")  # 快捷键
            new_action.triggered.connect(self.new_file)
            file_menu.addAction(new_action)
    
            # 打开动作
            open_action = QAction(QIcon("open.png"), "打开", self)
            open_action.setShortcut("Ctrl+O")
            open_action.triggered.connect(self.open_file)
            file_menu.addAction(open_action)
    
            # 保存动作
            save_action = QAction(QIcon("save.png"), "保存", self)
            save_action.setShortcut("Ctrl+S")
            save_action.triggered.connect(self.save_file)
            file_menu.addAction(save_action)
    
            # 分隔线
            file_menu.addSeparator()
    
            # 退出动作
            exit_action = QAction("退出", self)
            exit_action.setShortcut("Ctrl+Q")
            exit_action.triggered.connect(self.close)
            file_menu.addAction(exit_action)
    
        def create_toolbar(self):
            # 创建工具栏
            toolbar = self.addToolBar("工具栏")
    
            # 添加动作（与菜单动作共用）
            # new_action = QAction(QIcon("new.png"), "新建", self)
            new_action = QAction(QIcon(self.exec_path + "/icon.jpg"), "新建", self)
            new_action.triggered.connect(self.new_file)
            toolbar.addAction(new_action)
    
            open_action = QAction(QIcon("open.png"), "打开", self)
            open_action.triggered.connect(self.open_file)
            toolbar.addAction(open_action)
    
            save_action = QAction(QIcon("save.png"), "保存", self)
            save_action.triggered.connect(self.save_file)
            toolbar.addAction(save_action)
    
        def new_file(self):
            self.text_edit.clear()
            self.setWindowTitle("未命名文件")
    
        def open_file(self):
            file_path, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "文本文件 (*.txt)")
            if file_path:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.text_edit.setText(f.read())
                self.setWindowTitle(file_path)
    
        def save_file(self):
            file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "文本文件 (*.txt)")
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.text_edit.toPlainText())
                self.setWindowTitle(file_path)
                QMessageBox.information(self, "提示", "保存成功！")
    
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

# test1()

'''
6.2 对话框：交互提示与输入
PyQt6 提供多种内置对话框，用于显示提示、警告、确认信息，或获取用户输入、选择文件等。

示例：常用对话框
'''
def test2():
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QFileDialog, QInputDialog
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("对话框示例")
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    # 1. 信息对话框
    def show_info():
        QMessageBox.information(window, "信息", "这是一条信息提示！")
    
    # 2. 警告对话框
    def show_warning():
        QMessageBox.warning(window, "警告", "这是一条警告信息！")
    
    # 3. 确认对话框
    def show_confirm():
        result = QMessageBox.question(window, "确认", "你确定要退出吗？", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if result == QMessageBox.StandardButton.Yes:
            window.close()
    
    # 4. 文件选择对话框
    def select_file():
        file_path, _ = QFileDialog.getOpenFileName(window, "选择文件", "", "所有文件 (*.*)")
        QMessageBox.information(window, "选择结果", f"你选择的文件：{file_path}")
    
    # 5. 输入对话框
    def input_text():
        text, ok = QInputDialog.getText(window, "输入", "请输入你的名字：")
        if ok and text:
            QMessageBox.information(window, "问候", f"你好，{text}！")
    
    # 添加按钮
    info_btn = QPushButton("信息框")
    info_btn.clicked.connect(show_info)
    layout.addWidget(info_btn)
    # layout.addWidget(QPushButton("信息框", clicked=show_info)) # 等同上面3行
    layout.addWidget(QPushButton("警告框", clicked=show_warning))
    layout.addWidget(QPushButton("确认框", clicked=show_confirm))
    layout.addWidget(QPushButton("选择文件", clicked=select_file))
    layout.addWidget(QPushButton("输入框", clicked=input_text))
    
    window.show()
    sys.exit(app.exec())

# test2()

'''
6.3 多线程：避免界面卡顿
当应用执行耗时操作（如文件下载、数据处理）时，若在主线程中执行，会导致界面冻结无响应。解决方法是将耗时操作放在子线程中执行。

示例：多线程处理耗时任务
'''
def test3():
    from PyQt6.QtCore import QThread, pyqtSignal
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressBar, QLabel
    import sys
    import time

    class WorkerThread(QThread):
        progress_signal = pyqtSignal(int)
        finish_signal = pyqtSignal()

        def run(self):
            for i in range(1, 11):
                time.sleep(1)
                self.progress_signal.emit(i * 10)
            self.finish_signal.emit()

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("多线程示例")
    window.resize(300, 200)
    layout = QVBoxLayout(window)

    progress_bar = QProgressBar()
    progress_bar.setRange(0, 100)
    layout.addWidget(progress_bar)

    status_label = QLabel("等待任务开始...")
    layout.addWidget(status_label)

    # 关键：把线程保存到窗口实例，避免被垃圾回收
    window._thread = None

    def start_task():
        if window._thread and window._thread.isRunning():
            return  # 防止重复启动
        btn.setEnabled(False)
        status_label.setText("任务执行中...")
        window._thread = WorkerThread()
        window._thread.progress_signal.connect(update_progress)
        window._thread.finish_signal.connect(task_finish)
        window._thread.start()

    def update_progress(value):
        progress_bar.setValue(value)

    def task_finish():
        status_label.setText("任务完成！")
        btn.setEnabled(True)

    btn = QPushButton("开始耗时任务")
    btn.clicked.connect(start_task)
    layout.addWidget(btn)

    # 优雅退出：窗口关闭时等待线程结束
    def closeEvent(ev):
        if window._thread and window._thread.isRunning():
            window._thread.quit()
            window._thread.wait()
        ev.accept()

    window.closeEvent = closeEvent

    window.show()
    sys.exit(app.exec())

# test3()

'''
6.4 界面美化：QSS 样式表
QSS（Qt Style Sheet）是 PyQt6 的样式表语言，类似 CSS，可自定义组件的外观，打造现代化界面。

示例：QSS 美化界面
'''
def test4():
    from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QSS美化示例")
    window.resize(300, 250)
    
    # 设置全局QSS样式
    window.setStyleSheet("""
        QWidget {
            background-color: #f5f5f5;
        }
        QLabel {
            font-size: 14px;
            color: #333;
        }
        QLineEdit {
            font-size: 14px;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: white;
            color: black;
        }
        QLineEdit:focus {
            border-color: #2196F3;
            outline: none;
        }
        QPushButton {
            font-size: 14px;
            padding: 10px;
            background-color: #2196F3;
            color: white;
            border: none;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #1976D2;
        }
        QPushButton:pressed {
            background-color: #0D47A1;
        }
    """)
    
    layout = QVBoxLayout(window)
    layout.setSpacing(15)
    layout.setContentsMargins(30, 30, 30, 30)
    
    layout.addWidget(QLabel("用户名："))
    layout.addWidget(QLineEdit())
    
    layout.addWidget(QLabel("密码："))
    layout.addWidget(QLineEdit())
    
    layout.addWidget(QPushButton("登录"))
    
    window.show()
    sys.exit(app.exec())

# test4()

'''
6.5 自定义组件：扩展功能
当内置组件无法满足需求时，可通过继承现有组件自定义新组件，实现个性化功能。

示例：自定义计数器组件
'''
def test5():
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
    import sys
    
    # 自定义计数器组件
    class CounterWidget(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.count = 0
            self.init_ui()
    
        def init_ui(self):
            # 布局
            layout = QHBoxLayout(self)
            layout.setSpacing(10)
    
            # 减号按钮
            self.minus_btn = QPushButton("-")
            self.minus_btn.clicked.connect(self.decrement)
            layout.addWidget(self.minus_btn)
    
            # 计数标签
            self.count_label = QLabel("0")
            self.count_label.setStyleSheet("font-size: 16px; width: 40px; text-align: center;")
            layout.addWidget(self.count_label)
    
            # 加号按钮
            self.plus_btn = QPushButton("+")
            self.plus_btn.clicked.connect(self.increment)
            layout.addWidget(self.plus_btn)
    
        def increment(self):
            self.count += 1
            self.count_label.setText(str(self.count))
    
        def decrement(self):
            if self.count > 0:
                self.count -= 1
                self.count_label.setText(str(self.count))
    
    # 测试自定义组件
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("自定义组件示例")
    window.resize(200, 100)
    
    layout = QHBoxLayout(window)
    layout.addWidget(CounterWidget())
    layout.addWidget(CounterWidget())
    
    window.show()
    sys.exit(app.exec())

test5()