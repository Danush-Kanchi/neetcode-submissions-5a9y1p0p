class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s,hash_t={},{}
        if len(s)!=len(t):
            return False
        def letter_count(word,hashing):
            for x in word:
                if x in hashing:
                    hashing[x]+=1
                else: 
                    hashing[x]=1
            return hashing
        return letter_count(s,hash_s)==letter_count(t,hash_t)

