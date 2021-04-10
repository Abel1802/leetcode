#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# date: 2020.02.03
# updata: 2021-04-09
'''
    leetcode-1 twoSum
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Violent enumeration '''
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Hash '''
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 17]
    target = 9
    solution = Solution()
    print("The index: {}".format(solution.twoSum(nums, target)))
