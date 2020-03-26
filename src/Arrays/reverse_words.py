import collections
from typing import Tuple, List


def reverse_words_in_char_list(chars: List[str]) -> None:
    _reverse(chars)
    word_start, word_length = 0,0
    for i, char in enumerate(chars):
        if char == ' ':
            _reverse(chars, word_start, word_length)
            word_length = 0
        else:
            word_start = i if i > 0 and chars[i-1] == ' ' else word_start
            word_length += 1
    _reverse(chars, word_start, word_length)

def _reverse(chars: List[str], start:int = 0, length:int = None) -> None: 
    length = len(chars) if length is None else length
    for i in range (start, (start + (length//2))):
        complement = start + length - 1 - (i - start)
        chars[i], chars[complement] = chars[complement], chars[i]

message = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]
reverse_words_in_char_list(message)
print(message)