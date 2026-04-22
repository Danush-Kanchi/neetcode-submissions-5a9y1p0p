class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for x in nums:
            count[x]=count.get(x,0)+1
        buckets = [[] for i in range(len(nums) + 1)]
        for x,n in count.items():
            buckets[n].append(x)
        result=[]
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
              result.append(num)
              if len(result)==k:
                return result

        

        
        