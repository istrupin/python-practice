def hasPalindromicPermutation(string: str) -> bool:
    oddChars = set()
    for c in string:
        if c in oddChars:
            oddChars.remove(c)
        else:
            oddChars.add(c)
    return len(oddChars) <= 1


print(hasPalindromicPermutation('ivicc'))
