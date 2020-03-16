"""does wordbreak"""
from __future__ import absolute_import
from typing import List, Set, Dict


class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> List[str]:
        return self.word_break_memo(s, set(word_dict), {})

    def word_break_memo(self, s: str, dict_set: Set[str], memo: Dict[str, List[str]]) -> List[str]:
        res = []
        if not s:
            return res
        if s in memo:
            return memo[s]
        if s in dict_set:
            res.append(s)
        for i in range(1, len(s)):
            right = s[i:]
            left = s[:i]
            if left in dict_set:
                right_constituents = self.word_break_memo(right, dict_set, memo)
                if right_constituents:
                    for j in range(0, len(right_constituents)):
                        res.append(left + " " + right_constituents[j])
        memo.update({s: res})
        return res


x = Solution()
print(x.word_break("aaa", ["a", "aa", "aaa"]))
