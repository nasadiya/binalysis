import numpy as np
from matplotlib import pyplot as plt


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
        data_store = np.vstack((data_store[1:, ],
                                asst_obj.weighted_indicator()))
        graph1.set_ydata(data_store[:, 1])
        graph2.set_ydata(data_store[:, 2])
        graph1.set_xdata(data_store[:, 0] / 1e9)
        graph2.set_xdata(data_store[:, 0] / 1e9)
        plt.ylim([data_store[:, 1:].min(), data_store[:, 1:].max()])
        plt.xlim([data_store[:, 0].min()/1e9, data_store[:, 0].max()/1e9])
        plt.draw()
        plt.pause(0.01)
