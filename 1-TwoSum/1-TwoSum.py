# Last updated: 8/9/2025, 2:01:14 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}    
        #1 string
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        #2 string
        for char in t:
            counter[char] = counter.get(char, 0) - 1

        #check if its 0
        if set(counter.values()) != {0}:
            return False
        return True