"""
unzip and aggregate historical data
"""

import os
import json
import re
import numpy
import numpy as np
import pandas as pd
from src.time_space import realtime
from src.data_process.carpenter import matrix_merge

CONFIG_PATH = './historical_data_config.json'
COLUMNS_KLINES = json.load(open(CONFIG_PATH, 'r'))['COLUMNS_KLINES']
TIME_COLUMNS = json.load(open(CONFIG_PATH, 'r'))['TIME_COLUMNS']


def get_path(symbol, interval='1m', freq='1M'):
    return json.load(open(CONFIG_PATH, 'r'))[interval + freq][symbol]


def _aggregate_symbol(symbol, interval='1m', freq='1M', output=False):
    path = get_path(symbol, interval, freq)
    # list files in this path
    filenames = [fil for fil in sorted(os.listdir(path))
                 if re.findall(symbol, fil) != []]
    # run a loop to go through all files and append them into one df
    agg_data = numpy.ndarray(shape=(0, len(COLUMNS_KLINES)))
    for file in filenames:
        print("     Processing file: {} \n".format(file))
        agg_data = np.vstack((agg_data, (pd.read_csv(path+file)).values))
    del filenames
    # if the output is required
    if output:
        earliest_time_stamp = realtime(np.min(agg_data[:, 0]),
                                       date_time=True).strftime("%b%Y")
        latest_time_stamp = realtime(np.max(agg_data[:, 0]),
                                     date_time=True).strftime("%b%Y")
        file_name = "klines_from_" + earliest_time_stamp + "_to_" + \
                    latest_time_stamp + ".csv"
        df = pd.DataFrame(data=agg_data, columns=COLUMNS_KLINES)
        del agg_data
        df.to_csv(path + file_name)
        del df
        print("Data was output to the folder.\n")
    else:
        return agg_data, COLUMNS_KLINES


def aggregate_symbols(symbols: list, cols: str, interval='1m', freq='1M',
                      key="Open time"):
    # find the index of the column, the column should not be datetime
    ind = [COLUMNS_KLINES.index(col) for col in cols]
    ind_key = COLUMNS_KLINES.index(key)
    # download data and merge using key
    main_data = None
    for symbol in symbols:
        print(" Processing symbol : {} \n".format(symbol))
        temp_data, _ = _aggregate_symbol(symbol, interval, freq)
        if main_data is None:
            main_data = temp_data[:, [ind_key] + ind]
        else:
            main_data = matrix_merge(main_data, temp_data[:, [ind_key] + ind])
    final_cols = [sym + "_" + col for sym in symbols for col in cols]
    return main_data, [key] + final_cols
