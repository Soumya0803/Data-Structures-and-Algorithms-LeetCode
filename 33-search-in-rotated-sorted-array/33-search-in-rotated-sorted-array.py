class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(not nums):
            return -1
        pivot_index = self.find_pivot(nums) 
        result = self.bin_search(nums, target, 0, pivot_index-1)
        if(result!=-1):
            return result
        else:
            return self.bin_search(nums, target, pivot_index, len(nums)-1)
        
    def find_pivot(self, arr):
	
        element_to_compare = arr[-1]
        low = 0
        high = len(arr)-1    
        while(low <= high):
            mid = (low+high)//2
            if element_to_compare < arr[mid]:
                low = mid+1
            elif element_to_compare >= arr[mid]:
                high = mid-1
        return low    

    def bin_search(self, arr, value, low, high):     
        while(low <= high):
            mid = (low+high)//2
            if value<arr[mid]:
                high = mid-1
            elif value>arr[mid]:
                low = mid+1
            else:
                return mid
        return -1