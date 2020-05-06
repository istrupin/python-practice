from typing import Set, List

def make_change(amount:int, denominations:List[int]) -> List[List[int]]:
    res = []
    change_helper(amount, denominations, [], res)
    return res


def change_helper(amount:int, denominations:List[int], so_far:List[int], results:List[List[int]], memo = {}, index = 0):
    if amount == 0:
        results.append(so_far)
        return
    if amount < 0 or index == len(denominations):
        return
    change_helper(amount - denominations[index], denominations, so_far + [denominations[index]], results, memo, index)
    change_helper(amount, denominations, so_far, results, memo, index + 1)


def change_combinations(amount:int, denominations:List[int], index:int = 0, memo = {}) -> int:
    if amount == 0:
        return 1
    if amount < 0 or index == len(denominations):
        return 0
    key = (amount, index)
    if key in memo:
        print(f"getting from memo {key}")
        return memo[key]
    #print(f"Trying to create {amount} from {denominations[index:]}")
    res = change_combinations(amount - denominations[index], denominations, index, memo) + \
        change_combinations(amount, denominations, index + 1, memo)
    memo[key] = res
    return res

def change_combinations_bottom_up(amount: int, denominations:List[int]) -> int:
    ways_of_getting_n=[0] * (amount + 1)
    ways_of_getting_n[0] = 1
    for d in denominations:
        for i in range (d, amount+1):
            ways_of_getting_n[i] += ways_of_getting_n[i - d]

    return ways_of_getting_n[amount]


    


# print(make_change(4,[1,2,3]))
# print(change_combinations(4,[1,2,3]))
print(change_combinations_bottom_up(4,[1,2,3]))
