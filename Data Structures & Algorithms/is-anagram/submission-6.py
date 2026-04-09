class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashS, hashT = {} , {}
        for i in range(len(s)):
            hashS[s[i]]= hashS.get(s[i],0)+1
            hashT[t[i]]=hashT.get(t[i],0)+1
        print(hashS)
        print (hashT)
        for c in s:
            if hashS[c]!=hashT.get(c,0):
                return False
        return True
