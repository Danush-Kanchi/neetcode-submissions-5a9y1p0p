class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result={}
        for n in nums:
            result[n]=result.get(n,0)+1
        freq_order=sorted(result.keys(),key=lambda x:result[x],reverse=True)
        return freq_order[:k]
        
        