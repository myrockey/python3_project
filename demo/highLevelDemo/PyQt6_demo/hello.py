from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys
 
# 1. 创建应用实例（每个PyQt程序必须有且只有一个QApplication）
app = QApplication(sys.argv)
 
# 2. 创建主窗口
window = QWidget()
window.setWindowTitle("我的第一个PyQt6应用")  # 设置窗口标题
window.resize(400, 300)  # 设置窗口大小（宽x高）
 
# 3. 添加组件（标签）
label = QLabel("Hello PyQt6！", parent=window)
label.move(150, 130)  # 设置组件位置（x,y）
 
# 4. 显示窗口
window.show()
 
# 5. 启动应用事件循环
sys.exit(app.exec())

"""
一个标准的 PyQt6 程序包含 5 个核心步骤，所有复杂应用都基于此扩展：

创建 QApplication 实例：管理应用的事件循环和资源，是程序的 “大脑”；
创建窗口组件：QWidget 是所有可视化组件的基类，可作为主窗口或子容器；
添加子组件：如按钮、标签等，通过parent参数指定所属容器；
显示组件：调用show()方法让组件可见；
启动事件循环：app.exec()让程序进入循环，等待用户操作（如点击、输入）。

原文链接：https://blog.csdn.net/toungboy/article/details/154354031
"""