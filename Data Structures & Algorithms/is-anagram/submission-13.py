class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count=dict()
        for m in s:
            if m in count:
                count[m]+=1
            else:
                count[m]=1
        for n in t:
            if n in count:
                count[n]-=1
            else:
                return False
        for value in count.values():
            if value!=0:
                return False
            
        return True
