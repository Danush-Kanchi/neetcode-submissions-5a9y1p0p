class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set=set(nums)
        for num in num_set:
            
            if (num-1) not in num_set:
                current = num
                length = 0
                # While current exists in nums:
                while current in num_set:
                #   Increase length
                    length+=1
                #   Move current to the next number
                    current+=1

                # Update longest
                longest=max(longest,length)

        return longest
        