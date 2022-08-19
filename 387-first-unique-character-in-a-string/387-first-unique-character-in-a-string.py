class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        # find the index
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i     
        return -1
        