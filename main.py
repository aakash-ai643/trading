from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.fetch_data import get_market_data
from utils.order_execution import place_order

app = FastAPI()

# 🔥 CORS Setup ताकि API दूसरे प्रोजेक्ट से भी Call हो सके
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # किसी भी Domain से API Call कर सकते हैं
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/market")
def market_data(symbol: str):
    return get_market_data(symbol)

@app.post("/trade")
def trade(symbol: str, qty: float, order_type: str):
    return place_order(symbol, qty, order_type)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8500)  # Change Port if Needed
