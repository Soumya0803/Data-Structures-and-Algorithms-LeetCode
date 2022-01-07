class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(not nums):
            return -1
        pivot=self.find_pivot(nums)
        output=self.binary_search(nums,0,pivot-1,target)
        if output!= -1:
            return output
        else:
            return self.binary_search(nums,pivot,len(nums)-1,target)

            
    def find_pivot(self, nums):
        low=0
        high=len(nums)-1
        last_element = nums[-1]
        while(low<=high):
            mid=(high+low)//2
            if last_element<nums[mid]:
                low=mid+1
            elif last_element>=nums[mid]:
                high=mid-1
        return low
        
    def binary_search(self,nums,low,high,target):
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
                
                    