class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def return_count_dict(x):
            count_x=dict()
            for a in x:
                if a in count_x:
                    count_x[a]+=1
                else:
                    count_x[a]=1
            return count_x
        return return_count_dict(s)==return_count_dict(t)
