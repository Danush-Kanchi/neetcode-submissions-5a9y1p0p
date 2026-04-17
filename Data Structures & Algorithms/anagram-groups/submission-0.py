class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for x in strs:
            hashmap[tuple(sorted(x))].append(x)
        return list(hashmap.values())

