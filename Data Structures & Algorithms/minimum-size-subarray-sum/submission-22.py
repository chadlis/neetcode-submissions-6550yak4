class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        g, d = 0, 0
        s = 0
        lm = float("+inf")
        n = len(nums)
        while (d < n):

            if (s < target):
                d += 1
                s += nums[d-1]
            while s >= target:
                lm = min(lm, d - g)
                s -= nums[g]
                g += 1
        return 0 if lm == float("+inf") else lm





