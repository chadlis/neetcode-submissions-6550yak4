class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for k in range(n):
            print(f"{k=}")
            if k > 0 and nums[k-1] == nums[k]:
                continue
            l, r = k+1, n - 1
            print(f"{l=}")
            print(f"{r=}")
            while r-l > 0:
                if nums[l] + nums[r] + nums[k] == 0:
                    res.append([nums[l], nums[r], nums[k]])
                    print(res)
                    r -= 1
                    l += 1
                    while r > l and nums[r] == nums[r+1] :
                        print("saut r")
                        r -= 1
                    while r > l and nums[l] == nums[l-1]:
                        print("saut l")
                        l += 1
                elif nums[l] + nums[r] + nums[k] < 0:
                    l += 1
                else:
                    r -= 1
        return res



            