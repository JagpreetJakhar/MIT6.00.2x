import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
import itertools

def find_combination(choices, total):
    power_set = []
    for i in itertools.product([1,0], repeat = len(choices)):
        power_set.append(np.array(i))
    filter_set_eq = []
    filter_set_less = []
    for j in power_set:
        if sum(j*choices) == total:
            filter_set_eq.append(j)
        elif sum(j*choices) < total:
            filter_set_less.append(j)
    if len(filter_set_eq) > 0:
        minidx = min(enumerate(filter_set_eq), key=lambda x:sum(x[1]))[1]
        return minidx
    else:
        minidx = max(enumerate(filter_set_less), key = lambda x:sum(x[1]))[1]
        return minidx
