class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c