import numpy as np

def inverse_percentile(arr_data, num):
    """
    :param arr_data: an array with numbers
    :param num: the number you wish to know at which percentile is it in arr_data
    :return: percentile of num (in the context of arr_data)
    """
    arr_data = sorted(arr_data)
    i_arr = [i for i, x in enumerate(arr_data) if x > num]

    return i_arr[0] / len(arr_data) if len(i_arr) > 0 else 1


def equal_range_binning(arr_data, bins=10):
    """
    :param arr_data: an array with numbers
    :param bins: number of bins you wish to divide arr_data into
    :return: from min to max of arr_data make equal range bins according to bins; return a list of labels of
        length equal to length of arr_data
    """
    import pandas as pd
    return list(pd.cut(arr_data, bins, labels=range(bins)))

def create_equal_population_binning_func(arr_data, bins=10):
    """
    :param arr_data: an array with numbers
    :param bins: number of bins you wish to divide arr_data into
    :return: function that transforms values of another array into bin labels
    """
    if bins > len(arr_data):
        raise ValueError("The number of bins is greater than the array length!")

    split = np.array_split(np.sort(arr_data), bins)
    cutoffs = [x[-1] for x in split]
    cutoffs = cutoffs[:-1]

    print("Binning function created with cutoffs: {}".format(cutoffs))

    def equal_population_binning_transform(new_data):
        discrete = np.digitize(new_data, cutoffs, right=True)

        return discrete

    return equal_population_binning_transform

test = range(10)
test2 = range(1000)
bin_transformer = create_equal_population_binning_func(test, 5)
print(bin_transformer(test2))
