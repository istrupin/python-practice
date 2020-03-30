from typing import List

def coupleSum(target:int, values:List[int]) -> bool:
   valSet = set()
   for i in values:
       if(target - i in valSet):
           return True
       else:
            valSet.add(i)
   
   return False 


vals = [1,2,3,4,5,6]
print(coupleSum(17,vals))