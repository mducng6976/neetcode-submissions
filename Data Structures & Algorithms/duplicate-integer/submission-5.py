class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = []
        for i in range(len(nums)):
            if nums[i] in result:
                return True
            else:
                result.append(nums[i])
        return False



        