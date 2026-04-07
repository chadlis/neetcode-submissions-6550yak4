class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        counts = dict()
        for i in range(ls):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
            if t[i] in counts:
                counts[t[i]] -= 1
            else:
                counts[t[i]] = -1
        for count in counts.values():
            if count != 0:
                return False
        return True

        
        