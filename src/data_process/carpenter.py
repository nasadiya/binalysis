"""
Auxiliary code to assist in data manipulation
"""

import numpy as np


def matrix_merge(np_array1, np_array2, key_index=0, join_type='inner'):
    """
    !! Arrays must be sorted
    np_array : 2-D numpy arrays
    key_index : column index to merge them by.
    join_type : one of [inner, outer, left]
    """
    def aux_merge(array1, array2, select_keys):
        """
        Auxiliary function to merging
        """
        keys1 = np.isin(array1[:, key_index], select_keys,
                        assume_unique=True)
        keys2 = np.isin(array2[:, key_index], select_keys,
                        assume_unique=True)
        array1 = array1[keys1, :]
        array2 = array2[keys2, :]
        merged_data = np.hstack((array1, np.delete(array2, key_index, 1)))
        return merged_data

    # create sets of key columns to compare
    set1 = set(np_array1[:, key_index])
    # combine data sets
    if join_type == 'inner':
        set2 = set(np_array2[:, key_index])
        inner_keys = list(set1.intersection(set2))
        final_data = aux_merge(np_array1, np_array2, inner_keys)
    elif join_type == 'outer':
        set2 = set(np_array2[:, key_index])
        outer_keys = list((set1-set2).union(set2-set1))
        final_data = aux_merge(np_array1, np_array2, outer_keys)
    else:
        final_data = aux_merge(np_array1, np_array2, list(set1))
    return final_data
