class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        target = 0
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            required_sum = target - nums[i]
            while l < r:
                if nums[l] + nums[r] == required_sum:
                    result.append([nums[i], nums[l], nums[r]])# [i,l,r]
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < required_sum:
                    l += 1
                else:
                    r -= 1
        return result