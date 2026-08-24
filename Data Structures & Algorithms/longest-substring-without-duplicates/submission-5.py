class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i, j, l, lm = 0, 0, 0, 0
        found = set()
        if n > 0:
            found.add(s[0])
            l += 1
            lm = l
        while j < n - 1:
            if s[j + 1] not in found:
                l += 1
                found.add(s[j+1])
                j += 1
            else:
                lm = max(lm, l)
                while s[i] != s[j+1]:
                    found.remove(s[i])
                    i += 1
                    l -= 1
                i += 1
                j += 1
        return max(l, lm)






