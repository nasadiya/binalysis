"""
signal generator for the order book algo
This reads the incoming data to calibrate the signals and generate trades.
"""

import numpy as np


class SignalGen:
    """
    initial state of signals
    """
    trade = False
    buy = False
    sell = False

    def __init__(self, data_epoch: np.array):
        """
        :param data_epoch: data to start with. must generate a signal
        :returns : updates buy or sell signals.
        """
        # updates the data contained in the object
        self.data = data_epoch
        # initial data defines the window to be considered
        self.window = len(data_epoch)
        # updates the signal based on this
        self.update_signal(data_epoch)

    def update_signal(self, additional_data: np.array, window=None):
        """
        :param window: to optionally update the window of the signal data
        :param additional_data: additional data point
        :return: updates buy or sell signals
        """
        # compute data to be dumped from data that is contained.
        if window is not None:
            self.window = window

        l_additional_data = len(additional_data)
        # add from the additional data
        # if window is bigger than additional data
        if self.window > l_additional_data:
            # just in case window was entered to be more than total data
            self.window = min((l_additional_data + len(self.data)),
                              self.window)
            # take the required window from the combined data
            self.data = np.append(self.data[-(
                    self.window - l_additional_data):], additional_data)

        # if window is not greater than additional data
        else:
            # keep the latest "window" observations
            self.data = additional_data[-self.window:]

        # generate signal based on self.data; consider moving data part to
        # another method.
        pass
