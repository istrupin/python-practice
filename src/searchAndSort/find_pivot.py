from typing import List

def find_pivot(arr:List[str]) -> int :
    l, m, r = 0, len(arr) // 2,len(arr) - 1
    #see if l -> m is sorted, if so this is rotation point
    while l <= r:
        if l != m-1 and arr[l] <= arr[m - 1] and arr[m] <= arr[r]:
            return m
        elif arr[m] < arr[r]: #rotation is in first half
            r = m 
            m = r//2
        elif arr[l] <= arr[m]: #rotation is in 2nd half
            l = m+1
            m = (r+l)//2
    return -1

print(find_pivot(['b','c','a']))
print(find_pivot(['a','b','c']))
print(find_pivot(['c','d','e','a','b']))

