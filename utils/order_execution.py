import ccxt
from config import API_KEY, SECRET_KEY, EXCHANGE

exchange = getattr(ccxt, EXCHANGE)({
    "apiKey": API_KEY,
    "secret": SECRET_KEY
})


def place_order(symbol, qty, order_type):
    try:
        if order_type.lower() == "buy":
            order = exchange.create_market_buy_order(symbol, qty)
        elif order_type.lower() == "sell":
            order = exchange.create_market_sell_order(symbol, qty)
        else:
            return {"error": "Invalid order type"}
        return {"order_id": order['id'], "status": "Success"}
    except Exception as e:
        return {"error": str(e)}
