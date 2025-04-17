import ccxt
from config import API_KEY, SECRET_KEY, EXCHANGE

def get_market_data(symbol: str):
    try:
        exchange = getattr(ccxt, EXCHANGE)({
            "apiKey": API_KEY,
            "secret": SECRET_KEY
        })
        ticker = exchange.fetch_ticker(symbol)
        return {"symbol": symbol, "price": round(ticker['last'], 2)}
    except Exception as e:
        return {"error": str(e)}
