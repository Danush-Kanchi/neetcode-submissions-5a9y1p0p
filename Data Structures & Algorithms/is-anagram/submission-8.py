class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s=dict()
        c_t=dict()
        for m in s:
            if m in c_s:
                c_s[m]+=1
            else:
                c_s[m]=1
        for n in t:
            if n in c_t:
                c_t[n]+=1
            else:
                c_t[n]=1
        return c_t==c_s
