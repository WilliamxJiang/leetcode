# Last updated: 8/8/2025, 4:42:37 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1
        
        for valid in count.values():
            if valid != 0:
                return False
        return True