from typing import Set

def permutate(input: str) -> Set[str]:
    results = set()
    _permutation_helper("",input,results)
    return results

def _permutation_helper(so_far:str, letters_left:str, results:Set[str]) -> None:
    if len(letters_left) == 0:
        results.add(so_far)
        return;
    for i, c in enumerate(letters_left):
        new_ll = letters_left[0:i] + letters_left[i+1:len(letters_left)] if i < len(letters_left) else ""
        _permutation_helper(so_far + c, new_ll, results )


print(permutate("abc"))