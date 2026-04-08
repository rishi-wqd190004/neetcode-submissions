class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op = {}
        
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in op:
                return [op[diff],idx]
            op[val] = idx