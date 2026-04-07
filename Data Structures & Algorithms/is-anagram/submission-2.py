from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        counts = Counter()
        for i in range(ls):
            counts[s[i]] += 1
            counts[t[i]] -= 1
        for count in counts.values():
            if count != 0:
                return False
        return True

        
        