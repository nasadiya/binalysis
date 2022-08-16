"""
The package is designed to elicit order book information from the trading
platform. The present exercise is to establish a relationship between the
order book metrics and the drift in general.
"""

import json
from binance import Client
from src.order_book_weight import OrderBookWeight, order_book_data

client = Client(json.load(open("./keys.json"))["api_key"])

order_book_obj = OrderBookWeight(client, "BTCUSDT")

order_book_data(order_book_obj, 10)
