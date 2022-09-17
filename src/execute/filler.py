"""
Program to check the feed and execute the order

"""
import numpy as np

MAX_UNFILLED = 0.00001


def order_filler(stream: list, price: float, fill: list, action: str):
    """
    :param stream: A list of two numpy arrays. Each array is N x 2,
    first column is price and second is size. The first array is bids,
    the second array is asks.
    :param price: the price at which the order is to be executed.
    :param fill: same as the return item below.
    :param action: 'buy' or 'sell'
    :return: returns a list of a numpy N x 2 array and float. The first list
    consists of [price, size] of successful fills. The seconds number is
    unfilled order
    """
    if action not in ['buy', 'sell']:
        raise ValueError("Please enter a valid action: ['buy', 'sell']")

    action_bin = 1 if action == 'buy' else 0

    # selects bid or ask according to action of sell or buy
    depth = stream[action_bin]

    # sort the array by action
    # int(2 * action_bin - 1) thus becomes -1 to sort descending of the
    # action is to sell and 1 if the action is to buy, thus favorably
    # sorting the depth
    depth = depth[depth[:, 0].argsort()[::int(2 * action_bin - 1)]]
    depth_size = depth.shape[0]
    size = fill[1]
    count = 0

    # if there is more to sell, more orders to choose from, price is favorable
    def regularity(siz, prc, dep, act, dep_siz, cnt):
        if siz > MAX_UNFILLED and dep_siz > (cnt + 1):
            if act == 'buy':
                if prc >= dep:
                    return True
            if act == 'sell':
                if prc <= dep:
                    return True
        return False

    # when regularity conditions are satisfied
    while regularity(size, price, depth[count, 1], action, depth_size, count):

        whats_left = max(0.0, size - depth[count, 1])
        fill[0] = np.vstack((fill[0], [depth[count, 0], size - whats_left]))
        size = whats_left
        count += 1
    fill[1] = size

    return fill, price


def initiate_order(live_stream, price: float, fill: list, action_stream):
    """
    takes order_filler and a live stream object and runs it till the order is
    filled. this should ideally be able to be stopped based on another
    trigger which asks the order to cease at user's will
    :param live_stream: object which can be pinged to update the next tick
    of the data.
    :param price: price at (or better) at which the trade is desired.
    :param fill: a list of a numpy N x 2 array and float. The first list
    consists of [price, size] of successful fills. The seconds number is
    unfilled order
    :param action_stream: a stream which either results in 'buy','sell' or
    'hold'
    :return: same as fill above
    """
    while action_stream.status() != 'hold':
        # if there is any order to be filled execute else break
        if fill[1] >= MAX_UNFILLED:
            fill, _ = order_filler(live_stream.depth(), price, fill,
                                   action_stream.status())
        else:
            break

    return fill
