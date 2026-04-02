class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += str((len(word))) + ":" + word

        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            length = int(s[i:j])

            start = j + 1 
            end = start + length
            ans.append(s[start:end])

            i = end

        return ans
