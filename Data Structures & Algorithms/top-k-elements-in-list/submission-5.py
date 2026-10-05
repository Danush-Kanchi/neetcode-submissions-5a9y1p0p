class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

            # 1. Count frequencies
            freq = {}
            for n in nums:
                freq[n]=freq.get(n,0)+1
            # 2. Create buckets
            buckets = [[] for _ in range(len(nums) + 1)]

            # 3. Put each number into its frequency bucket
            for number,frequency in freq.items():
                buckets[frequency].append(number)


            # 4. Walk buckets backwards
            result = []


            # 5. Once result contains k elements, return it
            for i in range(len(nums),0,-1):
                for num in buckets[i]:
                    result.append(num)
                    if len(result)==k:
                        return result
         
        
        