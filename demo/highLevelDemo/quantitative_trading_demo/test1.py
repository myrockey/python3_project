#!/usr/bin/python3

import yfinance as yf
import time, random

'''
A 股别硬啃 Yahoo，(老限流：YFRateLimitError('Too Many Requests. Rate limited. Try after a while.'))
Tushare 一行代码就能拿 600519 全历史，
AkShare 无 key 无限速，
'''

def get_history(symbol, start, end):
    # ❌ 删除 session 参数，让 yfinance 自己管理
    data = yf.download(
        symbol, start=start, end=end,
        interval='1d', auto_adjust=False,
        progress=False, threads=False,   # 单线程 + 无进度条
    )
    time.sleep(random.randint(2, 4))     # 防 429
    return data.head()

# print(get_history('600519.SS', '2022-01-01', '2023-01-01'))

def get_history_new():
    import akshare as ak

    df = ak.stock_zh_a_hist(symbol='600519',
                            period='daily',
                            start_date='20220101',
                            end_date='20230101',
                            adjust='')        # 不复权
    print(df.head())

# get_history_new()

def get_show():
    import yfinance as yf
    import pandas as pd
    import matplotlib.pyplot as plt

    # 获取股票数据
    symbol = "600519.SS"
    start_date = "2022-01-01"
    end_date = "2023-01-01"

    data = yf.download(symbol, start=start_date, end=end_date)
    # 简单的数据分析
    print(data.describe())

    # 绘制股价走势图
    data['Close'].plot(figsize=(10, 6), label=symbol)
    plt.title(f"{symbol} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

# get_show()

def get_show_new():
    import akshare as ak
    import pandas as pd
    import matplotlib.pyplot as plt

    # 股票代码与区间（akshare 用 YYYYMMDD）
    symbol = "600519"          # A 股代码（自动复权，如需不复权 adjust=""）
    start_date = "20220101"
    end_date = "20230101"

    # ① 获取日线数据（返回 DataFrame，字段与 Yahoo 基本一致）
    data = ak.stock_zh_a_hist(symbol=symbol,
                              period='daily',
                              start_date=start_date,
                              end_date=end_date,
                              adjust='')      # 不复权；后复权用 'hfq'
    # ② 把日期列设为索引，方便后续画图
    data.rename(columns={'日期': 'Date'}, inplace=True)
    data.set_index('Date', inplace=True)
    data.index = pd.to_datetime(data.index)   # 转时间索引

    # ③ 简单统计
    print(data[['开盘', '最高', '最低', '收盘', '成交量']].describe())

    # ④ 绘制收盘价走势图
    data['收盘'].plot(figsize=(10, 6), label=f"{symbol} Close")
    plt.title(f"{symbol} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price (CNY)")
    plt.legend()
    plt.show()

# get_show_new()

def show_history():
    import yfinance as yf
    import pandas as pd
    import matplotlib.pyplot as plt

    # 获取股票数据
    symbol = "600519.SS"
    start_date = "2021-01-01"
    end_date = "2023-01-01"

    data = yf.download(symbol, start=start_date, end=end_date)

    # 计算移动平均
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()

    # 初始化交叉信号列
    data['Signal'] = 0

    # 计算交叉信号
    data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1
    data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1

    # 计算每日收益率
    data['Daily_Return'] = data['Close'].pct_change()

    # 计算策略信号的收益率（shift(1) 是为了避免未来数据的偏差）
    data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']

    # 计算累计收益
    data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

    # 输出策略表现
    strategy_performance = {
        'Total Return': data['Cumulative_Return'].iloc[-1] - 1,
        'Annualized Return': (data['Cumulative_Return'].iloc[-1] ** (252 / len(data))) - 1,
        'Max Drawdown': (data['Cumulative_Return'] / data['Cumulative_Return'].cummax() - 1).min(),
    }

    print("策略表现:")
    for key, value in strategy_performance.items():
        print(f"{key}: {value:.4f}")

    # 绘制累计收益曲线
    plt.figure(figsize=(10, 6))
    plt.plot(data['Cumulative_Return'], label='Strategy Cumulative Return', color='b')
    plt.plot(data['Close'] / data['Close'].iloc[0], label='Stock Cumulative Return', color='g')
    plt.title("Cumulative Return of Strategy vs. Stock")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.show()

# show_history()

'''
移动平均交叉策略回测
回测是在历史市场数据上模拟和评估一个交易策略的过程。

以下是一个简单的移动平均交叉策略回测的实例代码，策略是在 50 日均线上穿越 200 日均线时买入，下穿越时卖出，策略的表现输出了总收益、年化收益和最大回撤等指标。
'''
def show_history_new():
    import akshare as ak
    import pandas as pd
    import matplotlib.pyplot as plt

    # 1. 参数（AkShare 用 YYYYMMDD）
    symbol      = "600519"          # 贵州茅台
    start_date  = "20210101"
    end_date    = "20230101"

    # 2. 获取日线（不复权，字段重命名为 Yahoo 风格）
    df = ak.stock_zh_a_hist(symbol=symbol,
                            period='daily',
                            start_date=start_date,
                            end_date=end_date,
                            adjust='')          # 不复权；后复权用 'hfq'

    # 3. 字段映射 → Yahoo 风格列名
    df = df.rename(columns={
        '日期': 'Date',
        '开盘': 'Open',
        '最高': 'High',
        '最低': 'Low',
        '收盘': 'Close',
        '成交量': 'Volume'
    })
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date').sort_index()

    # 4. 后续逻辑与原函数完全一致
    # 计算移动平均
    df['SMA_50']  = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()

    # 交叉信号
    df['Signal'] = 0
    df.loc[df['SMA_50'] > df['SMA_200'], 'Signal'] = 1
    df.loc[df['SMA_50'] < df['SMA_200'], 'Signal'] = -1

    # 日收益 & 策略收益
    df['Daily_Return']     = df['Close'].pct_change()
    df['Strategy_Return']  = df['Signal'].shift(1) * df['Daily_Return']
    df['Cumulative_Return'] = (1 + df['Strategy_Return']).cumprod()

    # 策略表现
    strategy_performance = {
        'Total Return': df['Cumulative_Return'].iloc[-1] - 1,
        'Annualized Return': (df['Cumulative_Return'].iloc[-1] ** (252 / len(df))) - 1,
        'Max Drawdown': (df['Cumulative_Return'] / df['Cumulative_Return'].cummax() - 1).min(),
    }
    print("策略表现:")
    for key, value in strategy_performance.items():
        print(f"{key}: {value:.4f}")

    # 绘图
    plt.figure(figsize=(10, 6))
    plt.plot(df['Cumulative_Return'], label='Strategy Cumulative Return', color='b')
    plt.plot(df['Close'] / df['Close'].iloc[0], label='Stock Cumulative Return', color='g')
    plt.title("Cumulative Return of Strategy vs. Stock")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.show()

show_history_new()

# 请注意，这只是一个简单的实例，实际应用中需要更复杂的策略和更多的考虑因素。