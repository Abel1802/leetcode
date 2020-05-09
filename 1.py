#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# date: 2020.02.03
'''
    leetcode-1 twoSum
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # using dict
        dic = {}
        for ind, num in enumerate(nums):
            dic[num] = ind
        for i, num in enumerate(nums):
            j = dic.get(target - num)
            if j is not None and j != i:
                return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 17]
    target = 9
    solution = Solution()
    print("the index: {}".format(solution.twoSum(nums, target)))
