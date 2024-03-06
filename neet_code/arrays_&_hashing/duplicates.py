class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        freq = {} 
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
            if t[i] in freq:
                freq[t[i]] -= 1
            else:
                freq[t[i]] = -1
        
        for k,v in freq.items():
            if v != 0:
                return False
        return True