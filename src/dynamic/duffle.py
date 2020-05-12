from typing import List, Tuple


def fill_duffle(max_capcacity: int, cakes: List[Tuple[int, int]]):
    # weight, value
    max_for_i_weight = [0] * (max_capcacity + 1)
    for i in range(max_capcacity + 1):
        for w, v in cakes:
            if i > 0 and w == 0 and v > 0:
                return float('inf')
            if w <= i:
                max_for_i_weight[i] = max(max_for_i_weight[i],
                                          v + max_for_i_weight[i - w])
    return max_for_i_weight[max_capcacity]


print(fill_duffle(5, [(2, 90), (3, 100), (5, 150)]))
print(fill_duffle(0, [(2, 90), (3, 100), (5, 150)]))
print(fill_duffle(0, [(0, 90), (3, 100), (5, 150)]))
print(fill_duffle(1, [(0, 90), (3, 100), (5, 150)]))
