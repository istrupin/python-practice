from typing import List

def find_pivot(arr:List[str]) -> int :
    l, m, r = 0, len(arr) // 2,len(arr) - 1
    #see if l -> m is sorted, if so this is rotation point
    while l <= r:
        m = l + ((r - l) // 2)
        if arr[m-1] > arr[m]:
            return m
        elif arr[l] <= arr[m] and arr[m] <= arr[r]:
            return l
        elif arr[m] >= arr[l]: #go right
            l = m + 1
        else:
            r = m - 1        
    return -1

print(find_pivot(['b','c','a']))
print(find_pivot(['b','c','d','a']))
print(find_pivot(['a','b','c','d']))
print(find_pivot(['c','d','e','a','b']))
print(find_pivot(['c','d','e','f','a','b']))

