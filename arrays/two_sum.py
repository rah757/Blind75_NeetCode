from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = 0
        visited = {}
        for i in nums:
            if target - i in visited:
                return [visited[target - i], pos]
            visited[i] = pos
            pos += 1
