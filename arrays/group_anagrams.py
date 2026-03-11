from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            dic = {}
            for char in word:
                dic[char] = dic.get(char, 0) + 1
            key = tuple(sorted(dic.items()))
            result[key].append(word)
        return list(result.values())
