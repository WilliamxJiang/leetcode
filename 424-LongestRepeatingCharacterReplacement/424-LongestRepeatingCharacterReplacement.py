# Last updated: 8/9/2025, 4:36:35 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        left = 0
        max_count= 0
        best = 0

        for r, char in enumerate(s):
            count[char] += 1
            max_count = max(max_count, count[char])
        
            while (r-left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, r-left + 1)
        return best