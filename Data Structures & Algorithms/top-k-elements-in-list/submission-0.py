from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        heap = []

        for key, val in d.items():
            if len(heap) < k:
                heapq.heappush(heap, [val, key])
            else:
                if val > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [val, key])

        return [i[1] for i in heap]

      

        