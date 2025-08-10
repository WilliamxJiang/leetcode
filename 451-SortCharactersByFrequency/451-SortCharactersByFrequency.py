# Last updated: 8/10/2025, 3:40:32 PM
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #count words, use a dictionary
        #convert list of tuples - custom comparator, slice top k

        word_count = {}
        for word in words:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1
        sorted_words = sorted(word_count.items(), key = lambda x: (-x[1], x[0]))

        return [word for word, count in sorted_words[:k]]