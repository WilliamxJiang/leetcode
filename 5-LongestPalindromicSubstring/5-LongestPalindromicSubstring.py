# Last updated: 8/11/2025, 10:07:31 AM

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #edge cases return single interval

        if not intervals:
            return[]
        
        #sort by start time
        intervals = sorted(intervals, key=lambda x:x[0])
        merged: List[List[int]] = []
        
        #seed with the first interval so we can look back at merged[-1]
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            start, end = intervals[i] 
            last_start, last_end = merged[-1]
            if start <= last_end:
                merged[-1][1] = max(last_end, end) #extend the end, keep the start the same cuz we sorted the start
            else:
                merged.append([start, end])

        return merged