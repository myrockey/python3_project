#!/usr/bin/python3

import os,sys

def bar_chart():
    from pyecharts.charts import Bar
    # 准备数据
    x_data = ['一月', '二月', '三月', '四月', '五月']
    y_data = [10, 20, 15, 25, 30]

    # 创建柱状图
    bar_chart = Bar()
    bar_chart.add_xaxis(x_data)
    bar_chart.add_yaxis('销售额',y_data)
    # 也可以传入路径参数，如 bar_chart.render("bar_chart.html")
    # print(sys.argv[0]) # d:/projects/python3_project/demo/highLevelDemo/pyecharts_demo/test1.py
    # print(__file__)    # d:/projects/python3_project/demo/highLevelDemo/pyecharts_demo/test1.py
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    filename =  exec_path + '/bar_chart.html'
    bar_chart.render(filename)
    # 如果在 bar_chart.render() 中不指定文件路径，Pyecharts 默认会在当前工作目录下生成一个名为 "render.html" 的文件，即生成的图表将保存在 "render.html" 文件中。
# bar_chart()

# 实例中图表的标题是 "月度销售额柱状图"，横轴是月份，纵轴是销售额，可以根据实际需求调整数据和图表配置：
def bar_chart2():
    from pyecharts import options as opts
    from pyecharts.charts import Bar

    # 准备数据
    x_data = ['一月', '二月', '三月', '四月', '五月']
    y_data = [10, 20, 15, 25, 30]

    # 创建柱状图
    bar_chart = Bar()
    bar_chart.add_xaxis(x_data)
    bar_chart.add_yaxis("销售额", y_data)

    # 配置图表
    bar_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="月度销售额柱状图"),
        xaxis_opts=opts.AxisOpts(name="月份"),
        yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
    )

    # 渲染图表
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    filename =  exec_path + '/bar_chart2.html'
    bar_chart.render(filename)

# bar_chart2()

# 以下是一个简单的例子，演示了如何使用 pyecharts 切换主题：
def bar_char3():
    from pyecharts import options as opts
    from pyecharts.charts import Bar
    # 内置主题类型可查看 pyecharts.globals.ThemeType
    from pyecharts.globals import ThemeType

    # 准备数据
    x_data = ['一月', '二月', '三月', '四月', '五月']
    y_data = [10, 20, 15, 25, 30]

    # 创建柱状图
    bar_chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))  # 初始主题，主题只能在这设置theme
    bar_chart.add_xaxis(x_data)
    bar_chart.add_yaxis("销售额", y_data)

    # 配置图表
    bar_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="月度销售额柱状图"),
        xaxis_opts=opts.AxisOpts(name="月份"),
        yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
    )    

    # 渲染图表
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    filename =  exec_path + '/bar_chart3.html'
    bar_chart.render(filename)

# bar_char3()

def bar_char5():
    from pyecharts import options as opts
    from pyecharts.charts import Bar

    # 准备数据
    x_data = ['一月', '二月', '三月', '四月', '五月']
    y_data = [10, 20, 15, 25, 30]

    # 创建柱状图
    bar_chart = Bar()
    bar_chart.add_xaxis(x_data)
    bar_chart.add_yaxis("销售额", y_data)

    # 配置全局属性
    bar_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="月度销售额柱状图", subtitle="副标题"),
        xaxis_opts=opts.AxisOpts(name="月份"),
        yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
        legend_opts=opts.LegendOpts(pos_left="center", pos_top="top"),
        toolbox_opts=opts.ToolboxOpts(),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )

    # 渲染图表
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    filename =  exec_path + '/bar_chart5.html'
    bar_chart.render(filename)

bar_char5()