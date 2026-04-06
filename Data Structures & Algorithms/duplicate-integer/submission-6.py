class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        nums.sort()
        for i in range(0,length-1):
            if nums[i]==nums[i+1]:
                return True
                exit()
        return False