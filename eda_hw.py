import pandas as pd
import numpy as np
import math
import pdb

def average(series):
    
    avg = sum(series)/len(series)
    return avg
pass
    """
    implements the average of a pandas series from scratch
    suggested functions:
    len(list)
    sum(list)
    you should get the same result as calling .mean() on your series
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mean.html
    See numpy documenation for implementation details:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    """

def standard_deviation(series):
    
    total = 0
    for i in series:
            total = total + (i - average(series) ** 2
    SD = math.sqrt(total / len(series)-1))
    return SD
pass    
    """
    implements the sample standard deviation of a series from scratch
    you may need a for loop and your average function
    also the function math.sqrt
    you should get the same result as calling .std() on your data
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.std.html
    See numpy documenation for implementation details:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html
    """


def median(series):
    
    x = len(series)
    proper = sorted(x)
    if len(proper)%2 == 0
        i = len(proper)/2
        median = (proper[i] + proper[i-1])/2
    else:
        i = len(proper)/2
        median = proper[i-1]
    return median
pass    
    
    """
    finds the median of the series from scratch
    you may need to sort your values and use
    modular division
    this number should be the same as calling .median() on your data
    See numpy documenation for implementation details:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html
    https://pandas.pydata.org/pandas-docs/version/0.23.0/generated/pandas.Series.median.html
    """

