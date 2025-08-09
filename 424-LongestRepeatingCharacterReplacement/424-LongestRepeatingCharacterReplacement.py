# Last updated: 8/9/2025, 4:10:21 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        l = 0
        maxCount = 0
        result = 0

        for r, char in enumerate(s):
            count[char] += 1
            maxCount = max(maxCount, count[char])

            #if replacements needed > k
            while (r-l+1) - maxCount > k:
                count[s[l]] -= 1
                l += 1
            best = max(maxCount, r-l+1)
        return best