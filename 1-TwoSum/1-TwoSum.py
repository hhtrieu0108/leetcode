# Last updated: 5/25/2025, 10:26:16 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_idx = []
        for idx1, first_num in enumerate(nums):
            for idx2, second_num in enumerate(nums):
                if idx1 == idx2:
                    continue
                if first_num + second_num == target:
                    list_idx.extend([idx1, idx2])
                    return list_idx
        # numMap = {}
        # n = len(nums)

        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in numMap:
        #         print(complement)
        #         print([numMap[complement], i])
        #     numMap[nums[i]] = i

        # return []  # No solution found