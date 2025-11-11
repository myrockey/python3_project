#!/usr/bin/python3

import subprocess
import platform
'''
1. 执行外部命令
subprocess.run() 是 subprocess 模块中最常用的函数之一。它可以执行一个外部命令，并等待命令完成。以下是一个简单的示例：
'''

def subprocess_run():
    # 执行1个简单的shell命令
    if platform.system() == 'Windows':
        # windows
        res = subprocess.run(
            ['cmd', '/c', 'dir', '/l'],   # /c 表示执行完退出
            capture_output=True,
            text=True,
            cwd=r'd:\projects\python3_project'  # 想列哪个目录就写哪个
        )
    else:
        # linux
        res = subprocess.run(['ls', '-l'], capture_output=True, text=True)

    # 打印命令的输出
    print(res.stdout)

# subprocess_run()

'''
2. 处理输入和输出
subprocess 模块允许你控制子进程的输入、输出和错误流。你可以将数据传递给子进程的标准输入，或者从子进程的标准输出和标准错误中读取数据。以下是一个示例：
'''
def subprocess_run2():
    # 执行一个命令，并将输入传递给子进程
    lines = 'hello\npython\nworld'
    if platform.system() == 'Windows':
        # findstr 支持大小写敏感匹配
        cmd = ['findstr', 'python']
    else:
        cmd = ['grep', 'python']

    result = subprocess.run(cmd, input=lines, capture_output=True, text=True)
    print(result.stdout, end='')

# subprocess_run2()

'''
3. 处理错误
subprocess 模块还允许你处理子进程的错误。如果子进程返回非零的退出状态码，subprocess.run() 会抛出一个 CalledProcessError 异常。你可以通过检查 result.returncode 来获取子进程的退出状态码。
'''
def subprocess_run3():
    try:
        if platform.system() == 'Windows':
            cmd = ['cmd', '/c', 'dir', 'nonexistent_file']
        else:
            cmd = ['ls', 'nonexistent_file']
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print(f"Error output: {e.stderr}")
# subprocess_run3()

'''
subprocess 模块的高级用法
1. 使用 Popen 类
subprocess.Popen 类提供了更底层的接口，允许你更灵活地控制子进程。你可以使用 Popen 来启动一个子进程，并在后台运行它，或者与它进行交互。
'''
def subprocess_popen():
    # 启动1个子进程
    process = subprocess.Popen(['ping','baidu.com'],stdout=subprocess.PIPE,text=True)
    # 读取子进程的输出
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    # 获取子进程的退出状态码
    return_code = process.poll()
    print(f"process finished with return code {return_code}")

# subprocess_popen()

'''
2. 使用管道
subprocess 模块允许你使用管道将多个命令连接在一起。你可以将一个命令的输出作为另一个命令的输入。
'''
def subprocess_popen2():
    if platform.system() == 'Windows':
        # Windows 版：dir /l  查找包含 "py" 的行
        p1 = subprocess.Popen(['cmd', '/c', 'dir', '/l'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['findstr', 'py'],
                            stdin=p1.stdout,
                            stdout=subprocess.PIPE,
                            text=True)

        output, _ = p2.communicate()
        print(output, end='')
    else:
        # 使用管道连接两个命令
        p1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'py'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)

        # 获取最终输出
        output = p2.communicate()[0]
        print(output)
        
subprocess_popen2()