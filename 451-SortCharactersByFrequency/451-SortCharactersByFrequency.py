# Last updated: 8/10/2025, 4:13:17 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #given array (int) an int (k), return most frequent kth values
        # all#s r same, returning the same #
        """Counting + sorting the list
        count = Counter(nums) #1: 3, 2: 2, 3: 1
        most_common = count.most_common(k)
        return [num for num, freq in most_common]"""

        #count frequencies
        freq = defaultdict(int) #1:3, 2: 2, 3: 1
        for num in nums:
            freq[num] += 1
        #create buckets, where index = freq, bucket length is len(nums)
        buckets = [[] for _ in range(len(nums)+ 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        #start w high freq bucket first
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result