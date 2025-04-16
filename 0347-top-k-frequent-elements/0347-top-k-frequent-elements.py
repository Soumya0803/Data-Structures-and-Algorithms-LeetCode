class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        heap =[]

        for key, val in counter.items():
            heapq.heappush(heap,(-val,key))

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res

