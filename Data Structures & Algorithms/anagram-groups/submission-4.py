class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for w in strs:
            result[tuple(sorted(w))].append(w)
        return list(result.values())
