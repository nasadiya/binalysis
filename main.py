"""
The package is designed to elicit order book information from the trading
platform. The present exercise is to establish a relationship between the
order book metrics and the drift in general.
"""

import sys
import json
from datetime import datetime
from binance import Client
from src.time_space import TimeType
from src.algo.order_book.order_book_weight import OrderBookWeight, \
    order_book_data

client = Client(json.load(open("./keys.json"))["api_key"])

order_book_obj = OrderBookWeight(client, "BTCUSDT")

present = TimeType(datetime.now())
# get a days worth of data
present.add_to(1, 'days')
time_milli = present.to_millis()


if __name__ == "__main__":

    hist_data = order_book_data(order_book_obj, time=time_milli)
    hist_data.to_csv('./historical_data.csv')
