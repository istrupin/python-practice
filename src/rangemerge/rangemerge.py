from typing import List, Tuple
from operator import itemgetter

def rangeMerge(ranges: List[Tuple[int, int]]) -> List[List[int]]:
    ranges.sort(key=itemgetter(0))
    merged = []
    current_range = ranges[0]

    for i in range (1, len(ranges)):
        next_range = ranges[i]
        if  current_range[1] >= next_range[0]:
            current_range = (current_range[0], max(current_range[1], next_range[1]))
        else:
            merged.append(current_range)
            current_range = next_range
    merged.append(current_range)

    return merged

x = 1234
a = [(1,10),(2,6),(3,5),(7,9)]
c = [(1,3), (3,4), (11,100), (4,9), (5,7)]

print(rangeMerge(c))
