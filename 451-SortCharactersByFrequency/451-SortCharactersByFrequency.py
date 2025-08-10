# Last updated: 8/10/2025, 3:40:17 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #given integer array nums
        #given integer k
        #return kth largest element including duplicates in sorted order
        #edge cases, k = length of the array if theres only one element, all duplicates = same #

        #keep a min-heap of about size k - since we want smallest k value

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num) #adds the element to the heap
            #if heap has > k values
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]