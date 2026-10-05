class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):

        # continue previous OR start fresh
            current_sum = max(nums[i],current_sum+nums[i])

        # update best answer
            max_sum = max(current_sum,max_sum)

        return max_sum