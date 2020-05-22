

def get_closing_paren(text: str, opening_index: int) -> int:
    nested = 0
    stack_len = 0
    for i, c in enumerate(text):
        if c == '(' and i >= opening_index:
            nested += 1
            stack_len += 1
        if c == ')':
            if nested == 1:
                return i
            else:
                nested -= 1
                stack_len -= 1
    return -1


t = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print(get_closing_paren(t, 10))
print(get_closing_paren(t, 28))
