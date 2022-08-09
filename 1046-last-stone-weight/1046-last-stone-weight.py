class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
         # first, negate all weight values in-place
        for i, s in enumerate(stones):
            stones[i] = -s
        heapify(stones)  
        while stones:
            s1 = -heappop(stones)  
            if not stones:  
                return s1
            s2 = -heappop(stones)  
            if s1 > s2:
                heappush(stones, s2-s1)  
            # else s1 == s2; both stones are destroyed
        return 0  