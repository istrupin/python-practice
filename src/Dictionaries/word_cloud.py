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
                self._add_word(current_word)
                current_word = []
            else:
                current_word.append(c)

    def _add_word(self, word: List[str]) -> None:
        a = 1
        word_str = ''.join(word)
        if word[0].isupper():
            word[0] = word[0].lower()
        #if upper case
            #if exists in lowercase
                #increment lowercase
            #else
            #   #increment or add uppercase
        #if lower case
            #check if exists in upper case:
                #remove uppercase
                #increment or add lowercase with 1 + how many uppercase had
            #else:
            #   increment or add lowercase 

    def _increment_or_add(self, word: str, inc: int = 1) -> None:
        if word in self._cloud_dict:
            self._cloud_dict[word] = self._cloud_dict[word] + inc
        else:
            self._cloud_dict[word] = inc


    def get_cloud(self) -> Dict[str, int]:
        return self._cloud_dict
