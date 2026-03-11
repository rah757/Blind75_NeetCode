class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = {}
        set2 = {}
        for i in s:
            set1[i] = set1.get(i, 0) + 1
        for i in t:
            set2[i] = set2.get(i, 0) + 1
        if set1 == set2:
            return True
        else:
            return False
