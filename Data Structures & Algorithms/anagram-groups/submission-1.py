class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for x in strs:
            count = [0]*26
            for i in x:
                index = ord(i)-ord('a')
                count[index]+=1
            hashmap[tuple(count)].append(x)
        return list(hashmap.values())
