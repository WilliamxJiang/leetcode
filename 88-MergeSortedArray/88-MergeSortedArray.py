# Last updated: 8/8/2025, 5:15:16 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m: ] = nums2
        nums1.sort()