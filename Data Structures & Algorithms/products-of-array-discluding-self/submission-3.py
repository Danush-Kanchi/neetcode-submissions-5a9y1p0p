class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        suffix=[1]*len(nums)
        for i in range(1,len(nums)):
            result[i]=result[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(len(nums)):
            result[i]=result[i]*suffix[i]
        return result