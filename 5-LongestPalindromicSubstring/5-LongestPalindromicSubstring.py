# Last updated: 8/11/2025, 9:49:18 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best_l = 0
        best_r = 0
        for center in range(n):
            #iterate over every possible center
            l = r = center
            while  l >= 0 and r < n and s[l] == s[r]:
                if (r-l) > (best_r - best_l):
                    best_l = l
                    best_r = r
                l -=1 
                r += 1
            l, r = center, center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l) > (best_r-best_l):
                    best_l, best_r = l, r
                l -= 1
                r += 1
        return s[best_l:best_r+1]
