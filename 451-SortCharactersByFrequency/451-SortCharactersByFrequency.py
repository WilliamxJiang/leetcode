# Last updated: 8/10/2025, 3:40:46 PM
class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Counting the frequency of each character, iterating this over and over to find total freq time
        """
        freq = Counter(s)
        #t: 1, r: 1, e: 2
        sorted_chars = sorted(freq.items(), key = lambda x: -x[1]) #
        return ''.join(char * count for char, count in sorted_chars)