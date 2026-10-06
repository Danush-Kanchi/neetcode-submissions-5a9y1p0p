import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:

            # add num to heap
            heapq.heappush(heap,num)


            # if we now have more than k elements,
            # remove the smallest
            if len(heap)>k:
                heapq.heappop(heap)


        # kth largest
        return heap[0]