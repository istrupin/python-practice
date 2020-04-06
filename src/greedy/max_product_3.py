from typing import List

def maxProd(vals: List[int]) -> int:
   highest, lowest = 0,0
   highest_2, lowest_2 = 0,0
   highest_3 = 0
   for idx, number in enumerate(vals):
       if idx > 1:
            highest_3 = max(lowest_2 * number, highest_2 * number)
       if idx > 0:
           highest_2 = max(highest_2, highest * number, lowest * number)
           lowest_2 = min(lowest_2, lowest * number, lowest * number)
       highest = max(highest, number)
       lowest = min(lowest, number)
   
   return highest_3

x = [4,2,1,6]
print(maxProd(x))