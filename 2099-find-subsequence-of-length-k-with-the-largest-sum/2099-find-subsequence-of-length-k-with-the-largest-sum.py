class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        h = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(h, (-nums[i], i))
            
        res = []
        for _ in range(k):
            _, idx = heapq.heappop(h)
            res.append(idx)
        res.sort()
        return [nums[idx] for idx in res]