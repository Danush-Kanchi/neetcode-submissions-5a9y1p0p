class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[] for i in range(len(nums)+1)]
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for num,fre in freq.items():
            bucket[fre].append(num)
        result=[]
        for i in range(len(bucket)-1,0,-1):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
                if len(result)==k:
                    return result
                
