class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1 for _ in range(length)]
        cum = 1
        for i in range(length):
            output[i] *= cum
            cum *= nums[i]
        cum = 1
        for i in range(length-1, -1, -1):
            output[i] *= cum
            cum *= nums[i]
        return output
    


        