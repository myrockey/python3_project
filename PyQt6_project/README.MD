35 MB 并不是你写的这几行 UI 代码本身，而是 PyInstaller 把整个 Python 解释器 + PyQt6（含 QML/QtQuick 原生库）+ 所有依赖 一起打进去了。
只要用的 GUI 框架是 PyQt6，体积就小不下来；真要小，只能换方案或做“二次瘦身”。
为什么这么大
表格
复制
组件	大致占比
PyQt6 核心库（Qt6Core、Qt6Gui、Qt6Widgets…）	≈ 28 MB
Qt6 平台插件、样式插件、图像格式插件	≈ 6 MB
Python 解释器本体 + 标准库	≈ 5 MB
你的脚本 + 串口模块	< 0.5 MB
UPX 压缩后	还能再压 20–30 %
能快速做的“瘦身”步骤
用 UPX 压缩（立竿见影）
bash
复制
pip install upx
# 下载 https://github.com/upx/upx/releases 解压到任意目录
pyinstaller -F -w main.py --upx-dir D:\tool\upx-4.0.0-win64
通常能从 35 → 23 MB 左右。
排除你用不到的 Qt 模块
在 .spec 文件里加 excludes 或在命令行加：
bash
复制
--exclude-module PyQt6.QtQml
--exclude-module PyQt6.QtQuick
--exclude-module PyQt6.QtWebEngine
可再减 3–5 MB。
用 Nuitka 编译 + UPX（比 PyInstaller 更激进）
bash
复制
pip install nuitka
python -m nuitka --standalone --onefile --windows-disable-console \
       --plugin-enable=qt-plugins main.py
同样能压到 20 MB 上下，且启动更快。
换 GUI 框架（真要极限小）
tkinter（自带，打包后 7–10 MB）
PySide2/6 官方也瘦不了多少
DearPyGui（基于 ImGui，10 MB 级）
ttkbootstrap（tkinter 美化，体积仍小）
结论
PyQt6 本身 20 MB+ 的存量摆在那，再“优化”也要 20 MB 左右。
35 MB → 23 MB是花 1 分钟加 UPX 就能拿到的收益，能接受就直接用。
如果必须 <10 MB，只能放弃 PyQt6，改 tkinter / DearPyGui / C++ Qt 静态编译。


补充：
upx 并不是 Python 包，PyPI 里自然找不到。
正确姿势只有两步：
去官网下载 Windows 版可执行文件
地址：https://github.com/upx/upx/releases
选 upx-4.2.2-win64.zip（或 win32），解压到任意目录，比如
D:\tools\upx\upx.exe
让 PyInstaller 调用它
在打包命令里加 --upx-dir 指向 含 upx.exe 的文件夹：
powershell
复制
pyinstaller -F -w main.py --upx-dir D:\tools\upx
或者把 upx.exe 所在路径直接加到系统 PATH，省略 --upx-dir 也行。
常见误区提醒
pip install upx → ❌ 不存在
pip install upx-py → 只是 Python 封装，不如直接原版 UPX 稳定
下载后双击 upx.exe 一闪而退是正常现象，它不是 GUI 程序。
效果
同一份代码，35.4 MB → 23 MB 左右，肉眼可见；
如果再加 --exclude-module PyQt6.QtQml --exclude-module PyQt6.QtQuick，还能再抠掉 2-3 MB。