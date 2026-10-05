class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for n in nums:
            hashmap[n]=hashmap.get(n,0)+1
        freq=sorted(hashmap,key=hashmap.get,reverse=True)
        print(freq)
        return freq[0:k]
        

        
        