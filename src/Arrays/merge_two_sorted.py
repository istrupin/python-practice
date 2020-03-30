from typing import List

def merge_sorted_lists(arr1: List[int], arr2: List[int]) -> List[int]:
    i, j = 0, 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
           yield arr2[j]
           j += 1
        elif j >= len(arr2):
            yield arr1[i]
            i += 1
        else:
            n1, n2 = arr1[i], arr2[j]
            if n1 <= n2:
                yield n1
                i += 1
            else:
                yield n2
                j += 1


a = [1,3,6,7]
b = [1]

g = list(merge_sorted_lists(a,b))
print(g)