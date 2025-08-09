# Last updated: 8/9/2025, 2:06:29 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #get rid of spaces and non characters
        #if string == reversed string

        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        
        if cleaned == cleaned[::-1]:
            return True
        return False