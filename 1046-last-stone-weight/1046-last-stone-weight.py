class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        def smash(maxHeap):
            if len(maxHeap) == 0: return 0
            elif len(maxHeap) == 1: return maxHeap[0]

            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x > y:
                heapq.heappush(maxHeap, -(x-y))

            return smash(maxHeap)

        return -(smash(maxHeap))
        