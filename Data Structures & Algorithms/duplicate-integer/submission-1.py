class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return bool(len(nums) - len(set(nums)))
        