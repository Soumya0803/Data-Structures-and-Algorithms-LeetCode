class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        li =0
        for i in range (1,len(nums)):
            if nums[i]!=nums[li]:
                li+=1
                nums[li]= nums[i]
        return li+1        