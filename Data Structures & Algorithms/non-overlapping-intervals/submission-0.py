class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        last_end = float('-inf')
        res = 0
        for start, end in intervals:
            if start < last_end:   
                res += 1
            else:                  
                last_end = end

        return res