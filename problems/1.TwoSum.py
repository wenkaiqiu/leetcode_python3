"""
https://leetcode.com/problems/two-sum/description/
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

    def __init__(self):
        nums = [11, 2, 7, 15]
        target = 9
        result = self.twoSum(nums, target)
        print(result)


Solution()
