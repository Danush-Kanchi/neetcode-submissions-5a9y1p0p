class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hasher={}
        for x in s:
            if x in hasher:
                hasher[x]+=1
            else:
                hasher[x]=1
        for y in t:
            if y in hasher:
                hasher[y]-=1
            else:
                return False
        for value in hasher.values():
            if value!=0:
                return False
        return True


