from typing import List

def reverseList(list:List):
    
    if list is None or len(list) == 0:
        return
    
    for i in range(0, len(list)//2):
        complement = len(list) - i - 1
        (list[i], list[complement]) = (list[complement], list[i])

a = ['a']
reverseList(a)
print(a)
    