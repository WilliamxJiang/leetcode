# Last updated: 8/10/2025, 2:48:07 PM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #for each index i in s, substring of length len(p) and check if its an anagram by count freq of substring and compare w frequency of p
        """res = []
        p_count = Counter(p)
        for i in range(len(s)-len(p) + 1):
            window = s[i:i+len(p)]
            if Counter(window) == p_count:
                res.append(i)
        return res"""

        #initialize 2 counter, one for p, one for current window s
        #build initial window counter for the fiurst len(p) chars of s
        #slide the window, char coming in, increment count, char going out, decrement, compare the counters
        res = []
        p_count = Counter(p)
        window_count = Counter(s[:len(p)])

        if window_count == p_count:
            res.append(0)
        for i in range(len(p), len(s)):
            window_count[s[i]] += 1
            #remove the leftmost character
            window_count[s[i-len(p)]] -= 1

            if window_count == p_count:
                res.append(i-len(p) + 1)
        return res