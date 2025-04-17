import pandas as pd

def moving_average_strategy(prices, short_window=10, long_window=50):
    df = pd.DataFrame(prices, columns=['price'])
    df['short_ma'] = df['price'].rolling(window=short_window).mean()
    df['long_ma'] = df['price'].rolling(window=long_window).mean()
    
    if df['short_ma'].iloc[-1] > df['long_ma'].iloc[-1]:
        return "BUY"
    else:
        return "SELL"
