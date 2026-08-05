class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st)) + '#' + st
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            length_str = ""
            while s[i] != '#':
                length_str += s[i]
                i += 1
            length = int(length_str)
            strs.append(s[i+1:i+length+1])
            i = i+length+1
        return strs

