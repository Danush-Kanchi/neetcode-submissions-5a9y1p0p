class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for x in nums:
            count[x]=count.get(x,0)+1
        heap=[]
        heapq.heapify(heap)
        for x,n in count.items():
            heapq.heappush(heap,(n,x))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x for n,x in heap]
        

        
        