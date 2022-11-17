"""
function to compute the weighted sum of order book and compare with the price
The script also uses a visualisation tool
"""

import numpy as np
import pandas as pd
from src.asset_object import AssetObject
from src.time_space import realtime


def order_book_data(asst_obj, time=None, size=100):
    """
    iteratively fetches tick data from the server and stores it as a data
    frame. Given an upper limit of time, it saves all data accumulated
    within that time. Otherwise, it stores a specific number of rows.
    :param asst_obj: asset object (order book object)
    :param time: upper limit of time
    :param size: number of rows of the data
    :return: returns a pandas data frame with the data
    """
    columns = len(asst_obj.weighted_indicator())
    # enter time as upper boundary, this will override size
    if time is not None:
        origin = asst_obj.server_time()
        placeholder = np.zeros(shape=(1, columns))
        print(realtime(origin), realtime(time))
        while origin <= time:
            new_data = np.array(asst_obj.weighted_indicator())
            placeholder = np.vstack((placeholder,
                                     new_data))
            origin = asst_obj.server_time()
        placeholder = placeholder[1:, ]
    # use the size provided if time is not provided
    else:
        placeholder = np.zeros(shape=(size, columns))
        for counter in range(size):
            placeholder[counter, :] = asst_obj.weighted_indicator()
    # convert to data frame
    dat = pd.DataFrame(data=placeholder, columns=asst_obj.columns)
    return dat


def weighted_sum(list_of_lists):
    """
    :param: list_of_lists: lists containing order size and order price
    :return: returns average price weighted by order size
    """
    array_of_floats = np.array(list_of_lists, dtype=np.float64)
    return array_of_floats.prod(axis=1).sum() / array_of_floats[:, 1]. \
        sum()


class OrderBookWeight(AssetObject):
    """
    To perform hypothesis tests on order book and price
    """

    def __init__(self, client_object, asset_moniker):
        super().__init__(client_object, asset_moniker)
        self.columns = ["time0", "time1", "ticker_price", "weighted_price"]

    def weighted_indicator(self, date_time=False):
        """
        :return: computes the instantaneous weighted price based on order
        book and also returns the average time and traded price.
        """
        time0 = self.server_time()
        order_book = self.order_book()
        price = self.ticker_price()
        time1 = self.server_time()

        return realtime(time0, date_time=True), realtime(time1,
                                                         date_time=True),  \
            price, weighted_sum(order_book['bids'] + order_book['asks'])
