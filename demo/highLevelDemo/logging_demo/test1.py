import logging

def test():
    logging.basicConfig(level=logging.DEBUG)

    logging.debug('这是1条调试信息')
    logging.info('这是1条普通信息')
    logging.warning('这是1条警告信息')
    logging.error('这是1条错误信息')
    logging.critical('这是1条严重错误信息')

# test()
'''
输出：
DEBUG:root:这是1条调试信息
INFO:root:这是1条普通信息
WARNING:root:这是1条警告信息
ERROR:root:这是1条错误信息
CRITICAL:root:这是1条严重错误信息
'''


def test2():
    # logging.basicConfig(level=logging.DEBUG) # 设置日志级别

    logging.debug('这是1条调试信息')
    logging.info('这是1条普通信息')
    logging.warning('这是1条警告信息')
    logging.error('这是1条错误信息')
    logging.critical('这是1条严重错误信息')

# test2()
'''
输出：
WARNING:root:这是1条警告信息
ERROR:root:这是1条错误信息
CRITICAL:root:这是1条严重错误信息

当未设置设置日志级别，debug调试信息和info普通信息都不输出
'''

'''
logging 模块的高级用法
1. 使用多个日志记录器
在大型项目中，你可能需要为不同的模块或组件创建独立的日志记录器。可以通过以下方式实现：
'''
def test3():
    import os
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    # 创建文件处理器
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    file_handler = logging.FileHandler(exec_path + "/my_logger.log",encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO) # debug信息不会输出

    # 设置日志格式
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # 记录日志
    logger.debug("这是一条调试信息")
    logger.info("这是一条普通信息")

# test3()
'''
my_logger.log文件日志:
2025-11-06 17:03:39,501 - my_logger - DEBUG - 这是一条调试信息
2025-11-06 17:03:39,502 - my_logger - INFO - 这是一条普通信息

控制台日志输出:
2025-11-06 17:03:39,502 - my_logger - INFO - 这是一条普通信息
'''

def test5():
    '''
    2. 日志过滤器
    你可以通过过滤器来控制哪些日志需要被记录。例如：
    '''
    class MyFilter(logging.Filter):
        def filter(self, record):
            '''
            日志记录器默认级别是 WARNING，
            INFO 比 WARNING 低，被整体过滤掉了，根本到不了「过滤器」这一步。
            解决：把 logger 级别设成 INFO 或更低
            logger.setLevel(logging.DEBUG)
            '''
            return (record.levelno in [logging.INFO,logging.WARNING,logging.ERROR])

    # 创建日志记录器
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG) # 解决：把 logger 级别设成 INFO 或更低
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    # 将过滤器添加到日志记录器
    console_handler.addFilter(MyFilter())
    # 将处理器添加到日志记录器
    logger.addHandler(console_handler)
    # 记录日志
    logger.debug('这是1条调试信息')
    logger.info('这是1条普通信息')
    logger.warning('这是1条警告信息')
    logger.error('这是1条错误信息')
    logger.critical('这是1条严重错误信息')

# test5()
'''
输出：
这是1条普通信息
这是1条警告信息
这是1条错误信息
'''

def test6():
    '''
    3. 日志轮转
    当日志文件过大时，可以使用 RotatingFileHandler 或 TimedRotatingFileHandler 实现日志轮转：
    '''
    from logging.handlers import RotatingFileHandler
    import os

    # 创建日志记录器
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG) # 解决：把 logger 级别设成 INFO 或更低
    # 创建文件处理器
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    '''
    exec_path + "/app.log"	日志文件路径，exec_path 是你提前拼好的目录，最终文件名是 app.log。
    maxBytes=1	单个文件最大字节数。这里设为 1 字节 → 每写 1 字节就触发轮转（演示/测试用，生产千万别这么写）。
    backupCount=4	最多保留 4 个旧文件。轮转时：
    app.log → app.log.1 → app.log.2 → … → app.log.4，超过就删除最老的。
    encoding='utf-8'	文件以 UTF-8 编码写入，防止中文乱码。
    '''
    file_handler = RotatingFileHandler(exec_path + "/app.log", maxBytes=1, backupCount=4,encoding='utf-8')
    # file_handler = RotatingFileHandler(exec_path + "/app.log", maxBytes=1e6, backupCount=3,encoding='utf-8') # 每个文件1M，最多备份3个文件
    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    # 记录日志
    logger.debug('这是1条调试信息')
    logger.info('这是1条普通信息')
    logger.warning('这是1条警告信息')
    logger.error('这是1条错误信息')
    logger.critical('这是1条严重错误信息')

test6()