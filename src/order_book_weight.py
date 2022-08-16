
"""
function to compute the weighted sum of order book and compare with the price
The script also uses a visualisation tool
"""

import numpy as np
import pylab as plt
from src.asset_object import AssetObject


def order_book_visualiser(asst_obj):

    n = 100
    n_temp = 0
    data_store = np.zeros(shape=(n, 3))
    plt.ion()
    graph1 = plt.plot(data_store[:, 0]/1e9, data_store[:, 1])[0]
    graph2 = plt.plot(data_store[:, 0]/1e9, data_store[:, 2])[0]
    plt.legend(['price', 'weighted_order'])

    while True:
        n_temp += 1
        print('\nData Counter : {} \n'.format(n_temp))
        data_store = np.vstack((data_store[1:, ], asst_obj.weighted_indicator()))
        graph1.set_ydata(data_store[:, 1])
        graph2.set_ydata(data_store[:, 2])
        graph1.set_xdata(data_store[:, 0] / 1e9)
        graph2.set_xdata(data_store[:, 0] / 1e9)
        plt.ylim([data_store[:, 1:].min(), data_store[:, 1:].max()])
        plt.xlim([data_store[:, 0].min()/1e9, data_store[:, 0].max()/1e9])
        plt.draw()
        plt.pause(0.01)


def order_book_data(asst_obj, size=100):
    columns = len(asst_obj.weighted_indicator())
    placeholder = np.zeros(shape=(size, columns))
    for counter in range(size):
        placeholder[counter, :] = asst_obj.weighted_indicator()
    return placeholder


class OrderBookWeight(AssetObject):
    """
    To perform hypothesis tests on order book and price
    """
    def __init__(self, client_object, asset_moniker):
        super().__init__(client_object, asset_moniker)
        self.columns = ["average_time", "average_price", "weighted_price"]

    def weighted_indicator(self):
        """2
        :return: computes the instantaneous weighted price based on order
        book and also returns the average time and traded price.
        """
        time_s = self.server_time()
        order_book = self.order_book()
        price = self.averager_price()
        time_f = self.server_time()

        def weighted_sum(list_of_lists):
            array_of_floats = np.array(list_of_lists, dtype=np.float64)
            return array_of_floats.prod(axis=1).sum() / array_of_floats[:1]. \
                sum()

        return (time_s + time_f) * 0.5, price, weighted_sum(
            order_book['bids'] +
            order_book['asks'])

