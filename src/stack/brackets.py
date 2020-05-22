

def is_valid(text: str) -> bool:
    openers = ['(', '{', '[', '|']
    closers = [')', '}', ']', '|']
    o_set = set(openers)
    c_set = set(closers)
    bracket_map = dict(zip(closers, openers))
    stack = []
    for c in text:
        if c in o_set:
            stack.append(c)
        if c in c_set:
            if len(stack) == 0 or bracket_map[c] != stack.pop():
                return False
    return len(stack) == 0


print(is_valid('(){}'))
print(is_valid('{()}'))
print(is_valid('()}}'))
print(is_valid('(){}|('))
print(is_valid('(){}|()|'))