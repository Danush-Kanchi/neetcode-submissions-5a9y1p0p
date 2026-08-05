class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in hash:
                return [hash[x],i]
            hash[nums[i]]=i
        

                   
        