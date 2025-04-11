# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mask = [0] * 26
        for ch1, ch2 in zip(s, t):
            mask[ord(ch1) - 97] += 1
            mask[ord(ch2) - 97] -= 1
        
        for val in mask:
            if val != 0:
                return False
        
        return True