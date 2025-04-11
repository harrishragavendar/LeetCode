# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indMap = {}
        for i, num in enumerate(nums):
            if num in indMap:
                return [i, indMap[num]]
            else:
                indMap[target - num] = i