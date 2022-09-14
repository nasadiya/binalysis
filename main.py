"""
The package is designed to elicit order book information from the trading
platform. The present exercise is to establish a relationship between the
order book metrics and the drift in general.
"""
import json
from datetime import datetime
from binance.spot import Spot
from src.time_space import TimeType
from src.algo.order_book.order_book_weight import OrderBookWeight, \
    order_book_data

client = Spot(json.load(open("./keys.json"))["api_key"])

order_book_obj = OrderBookWeight(client, "BTCUSDT")

present = TimeType(order_book_obj.server_time(), time_type='milliseconds')

t1 = present.to_millis()
# get a days worth of data
present.add_to(-1, 'days')
# time_milli = present.to_millis()
# order_book_data(order_book_obj, time=time_milli)
t0 = present.to_millis()
d = client.klines(symbol="BTCUSDT", interval= '1s', startTime=t0, endTime=t1)
# get only 60 seconds worth of klines in one shot.


if __name__ == "__main__":

    hist_data = order_book_data(order_book_obj, time=time_milli)
    hist_data.to_csv("datadump/historical_data.csv")
