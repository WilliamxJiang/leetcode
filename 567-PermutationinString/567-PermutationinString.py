# Last updated: 8/9/2025, 6:52:30 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #permutation is a rearrangement
        #permutation of s1 has same letter counts as s1
        ''' 
        slide a fixed-size window of length s1 over s2
        '''
        #s1 > s2, no permutation can exist
        if len(s1) > len(s2):
            return False
        #char frequency in s1
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        #set up sliding window, size of s1
        window_size = len(s1)
        window_count = {}

        #initialize window
        for i in range(window_size):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1
        
        if window_count == s1_count: #if first window matches
            return True

        #slide through s2
        for i in range(window_size, len(s2)):
            #add new character to window
            new_char = s2[i]
            window_count[new_char] = window_count.get(new_char, 0) + 1

        #remove previous characters window
            old_char = s2[i - window_size]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]
        #check if window matches the character freq
            if window_count == s1_count:
                return True
        return False