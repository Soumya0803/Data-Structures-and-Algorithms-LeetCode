class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}  # val -> index
         
        for i,n in enumerate(nums):
            if target-n in prevMap:
                return [prevMap[target-n],i]
            prevMap[n] =i
        