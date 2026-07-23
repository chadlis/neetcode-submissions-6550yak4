class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        lmax = 0
        for num in uniques:
            if (num - 1) in uniques:
                continue
            x = num
            ll = 1
            while (x + 1) in uniques:
                x += 1
                ll += 1
            if ll > lmax:
                lmax = ll
        return lmax
            
      





































            
            
            
            