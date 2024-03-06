class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        _dict = {}

        for i in range(len(s)):
            if s[i] in _dict:
                _dict[s[i]] += 1
            else:
                _dict[s[i]] = 1
            if t[i] in _dict:
                _dict[t[i]] -= 1  
            else:
                _dict[t[i]] = -1

        for v in _dict.values():
            if v != 0:
                return False

        return True