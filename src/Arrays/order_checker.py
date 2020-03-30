from typing import List

def check_order(di: List[int], ta: List[int], fulfilled: List[int]) -> bool:
    t, d = 0, 0

    for order in fulfilled:
        if d < len(di) and di[d] == order:
            d += 1
        elif t < len(ta) and ta[t] == order:
            t += 1
        else:
            return False
    return True


t = []
d = [2,4,6]
c =[2,4,6]

print(check_order(d,t,c))