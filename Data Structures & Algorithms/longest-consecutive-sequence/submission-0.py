class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        lmax = 0
        for num in uniques:
            if (num - 1) in uniques:
                continue
            x = num
            seq = {x}
            while (x + 1) in uniques:
                x += 1
                seq.add(x)
            if (ll:= len(seq)) > lmax:
                lmax = ll
        return lmax
            
      





































            
            
            
            