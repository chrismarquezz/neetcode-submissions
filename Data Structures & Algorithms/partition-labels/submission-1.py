class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_occurence = {}
        start = 0
        end = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last_occurence:
                last_occurence[s[i]] = i
        for i in range(len(s)):
            end = max(end, last_occurence[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res
