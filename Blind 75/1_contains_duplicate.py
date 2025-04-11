# https://leetcode.com/problems/contains-duplicate/
# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)