class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if d.get(num, False):
                return True
            d[num] = True
        return False
        