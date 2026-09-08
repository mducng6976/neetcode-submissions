class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in check:
                return [check[complement], i]
            else:
                check[num] = i