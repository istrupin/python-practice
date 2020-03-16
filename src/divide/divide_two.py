import sys

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor: return 1
        if divisor == 1: return dividend
        if dividend == -1 << 31 and divisor == -1: return 2147483647
        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        res = 0
        for power in range(32)[::-1]:
            if ((a >> power) - b) >= 0:
                res += 1<<power
                a -= b<<power
        return res if not negative else 0-res

# x = Solution()
# print(x.divide(-3,-2))


