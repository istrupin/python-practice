from typing import List

def maxGain(vals: List[int]) -> int:
    smallest = vals[0]
    max_gain = vals[1] - vals[0]
    for i in range(1,len(vals)):
        max_gain = max(max_gain, vals[i] - smallest)
        smallest = min(smallest, vals[i])
    return max_gain


# v = [10,7,5,8,11,9]
v = [9,8,7,5,1]
print(maxGain(v))