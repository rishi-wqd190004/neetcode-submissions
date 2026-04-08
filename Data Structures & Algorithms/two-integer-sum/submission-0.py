class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op = [0]
        diff = target - nums[0]
        for i in range(len(nums)):
            if diff == nums[i]:
                op.append(i)
        return op