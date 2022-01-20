class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = [0]*26
        for letter in p:
            count_p[ord(letter)-ord('a')] += 1
            
        count_s = [0]*26
        left = right = 0
        result = []
        while right < len(s):
            count_s[ord(s[right])-ord('a')] += 1
            if right-left == len(p):
                count_s[ord(s[left])-ord('a')] -= 1
                left += 1
            if count_s == count_p:
                result.append(left)
            right += 1
            
        return result