import yfinance as yf

def moving_average_crossover_strategy(ticker, short_window, long_window):
    # 获取黄金ETF数据
    gold_etf_data = yf.download(ticker, start="2020-01-01", end="2023-01-01")

    # 计算短期和长期移动平均线
    gold_etf_data['Short_MA'] = gold_etf_data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    gold_etf_data['Long_MA'] = gold_etf_data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # 交易信号：当短期均线上穿长期均线时买入，当短期均线下穿长期均线时卖出
    gold_etf_data['Signal'] = 0
    gold_etf_data.loc[gold_etf_data['Short_MA'] > gold_etf_data['Long_MA'], 'Signal'] = 1
    gold_etf_data.loc[gold_etf_data['Short_MA'] < gold_etf_data['Long_MA'], 'Signal'] = -1

    # 计算每日收益率
    gold_etf_data['Daily_Return'] = gold_etf_data['Close'].pct_change()

    # 计算策略每日收益率
    gold_etf_data['Strategy_Return'] = gold_etf_data['Signal'].shift(1) * gold_etf_data['Daily_Return']

    # 计算累积收益率
    gold_etf_data['Cumulative_Return'] = (1 + gold_etf_data['Strategy_Return']).cumprod()

    return gold_etf_data

if __name__ == "__main__":
    ticker_symbol = 'GLD'  # 黄金ETF的Ticker符号
    short_window = 5  # 短期移动平均线窗口大小
    long_window = 20  # 长期移动平均线窗口大小

    gold_etf_strategy_data = moving_average_crossover_strategy(ticker_symbol, short_window, long_window)

    # 输出策略数据
    print(gold_etf_strategy_data)
