from typing import Dict

def recursive_fib(n:int) -> int:
    if n <= 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)

def memo_fib(n:int, memo:Dict[int, int] = {}) -> int:
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = memo_fib(n - 1, memo) + memo_fib(n - 2, memo)
    return memo[n]

def bu_fib(n:int) -> int:
    if n <= 1:
        return n
    ar = [0,1]
    for i in range(2,n):
        next = ar[0] + ar[1];
        ar[0] = ar[1]
        ar[1] = next
    return ar[0] + ar[1]



print(recursive_fib(7))
print(memo_fib(7))
print(bu_fib(7))