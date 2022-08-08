class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:      

        #Turn the input array into a max heap
        score = [(-s, idx) for idx, s in enumerate(score)]
        heapq.heapify(score)

        output = [None] * len(score)
        count = 1

        while len(score):
            _, idx = heapq.heappop(score)

            if count == 1:
                output[idx] = 'Gold Medal'
            elif count == 2:
                output[idx] = 'Silver Medal'
            elif count == 3:
                output[idx] = 'Bronze Medal'
            else:
                output[idx] = str(count)

            count += 1

        return output
        