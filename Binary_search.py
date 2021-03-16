import numpy as np
from math import *

x = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
y = [10,14,19,26,27,31,33,35,42,44,50,60]
def Binary_search(y,x0):
    L = len(y)
    high = L; low = 0 # starting indexes
    mid = low + (high - low)/ 2
    MID = []
    # Check if mid value, lowest, or highest value
    if int(mid) == x0:
        return y[floor(mid)]
    elif low == x0:
        return y[low]
    elif high-1 == x0:
        return y[high-1]
    for i in range(floor(high/2)):
        mid = low + (high - low)/ 2
        MID.append(floor(mid))
        if int(mid) == x0:
            return y[floor(mid)],MID
        if x0 < mid:
            high = mid - 1
        else:
            low = mid + 1
print(Binary_search(y,11))

