from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        get_max_freq = lambda freqs : 0 if len(freqs) == 0 else freqs.most_common(1)[0][1]
        g, d = 0, 0
        n = len(s)
        res = 0
        freqs = Counter()
        maxfreq = 0
        while d < n:
            d += 1
            freqs[s[d-1]] += 1
            while ((d-g) - (maxfreq:=get_max_freq(freqs))) > k:
                freqs[s[g]] -= 1
                g += 1
            res = max(res, d-g)
        return res


                
                

            
