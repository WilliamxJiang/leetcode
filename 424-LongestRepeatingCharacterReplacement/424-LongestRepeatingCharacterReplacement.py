# Last updated: 8/9/2025, 2:58:27 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #dictionary count freq of characters
        char_count = {}
        #left pointer
        left = 0
        max_freq = 0
        max_length = 0

        #right pointer expanding the window
        for right in range(len(s)):
            #add current character to frequency count
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            #update the max frequency
            max_freq = max(max_freq, char_count[s[right]])

            #update window size
            window_size = right - left + 1
            if window_size - max_freq > k:
                #remove leftmost character
                char_count[s[left]] -= 1
                #move left pointer to shrink window
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length