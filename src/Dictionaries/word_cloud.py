from typing import Dict, List

class WordCloud:
    def __init__(self):
        self._cloud_dict = {}

        #only make word uppercase in dictionary if it is always upper case in original string

        self._skipped_chars = {',',';', '.', '?', '!'} #ignore these entirely
        self._delim = ' '

    def read_text(self, text: str) -> None:
        current_word = []
        for c in text:
            if c in self._skipped_chars:
                continue
            if c == self._delim:
                if len(current_word) > 0:
                    self._add_word(current_word)
                    current_word = []
            else:
                current_word.append(c)
        if len(current_word) > 0:
                    self._add_word(current_word)
                    current_word = []

    def _add_word(self, word: List[str]) -> None:
        orig = word[0]
        word[0] = word[0].upper()
        u_word = ''.join(word)
        word[0] = word[0].lower()
        l_word = ''.join(word)
        word[0] = orig

        if word[0].isupper():
            if l_word in self._cloud_dict:
                self._increment_or_add(l_word)
            else:
                self._increment_or_add(u_word)
        elif word[0].islower():
            if u_word in self._cloud_dict:
                ct = self._cloud_dict.pop(u_word)
                self._increment_or_add(l_word, ct+1)
            else:
                self._increment_or_add(l_word)

    def _increment_or_add(self, word: str, inc: int = 1) -> None:
        if word in self._cloud_dict:
            self._cloud_dict[word] = self._cloud_dict[word] + inc
        else:
            self._cloud_dict[word] = inc

    def get_cloud(self) -> Dict[str, int]:
        return self._cloud_dict


print(("").join(['a','b','c']))
wc = WordCloud()
wc.read_text('Lowercase. That word should be lowercase. However, on the other-hand, should be uppercase. However that is yet to be seen. Other-hand')
# wc.read_text('However. however')

print(wc.get_cloud())