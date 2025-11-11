#!/usr/bin/python3

# 实例 1. 基础配置
def app_log():
    import logging,os
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    # 配置日志
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename= exec_path + '/my_app.log',
        encoding='utf-8'
    )

    # 使用
    logger = logging.getLogger("my_app")
    logger.info("程序启动")

# app_log()

def module_log(moduleName):
    import logging,os
    # 创建记录器
    logger = logging.getLogger(moduleName)
    logger.setLevel(logging.DEBUG)

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    # 文件处理器
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    file_handler = logging.FileHandler(exec_path + '/' + moduleName + "_debug.log",encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # 格式化
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # 使用
    logger.debug("调试信息")  # 仅写入文件
    logger.warning("警告！")  # 同时输出到控制台和文件

module_log('my_module')