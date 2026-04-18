class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for x in nums:
            hashmap[x]=hashmap.get(x,0)+1
            
        result=[x[0] for x in sorted(hashmap.items(),key=lambda x:x[1],reverse=True)][0:k]
        return result
        

        
        