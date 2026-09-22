class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for words in strs:
            result[tuple(sorted(words))].append(words)
        return list(result.values())
        