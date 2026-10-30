class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_s={}
        for i in range(len(s)):
            hash_s[s[i]]=hash_s.get(s[i],0)+1
            hash_s[t[i]]=hash_s.get(t[i],0)-1
        for val in hash_s.values():
            if val!=0:
                return False
        return True