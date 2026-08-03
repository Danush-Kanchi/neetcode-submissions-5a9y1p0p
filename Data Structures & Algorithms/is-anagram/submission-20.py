class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        for m in s:
            count[m]=count.get(m,0)+1
        for n in t:
            count[n]=count.get(n,-1)-1
            if count[n] < 0:
                return False
           
        for value in count.values():
            if value!=0:
                return False
            
        return True
