#!usr/bin/env python3
# author fool
# date 2020-03-02
'''
    Leetcode-4 寻找两个正序数组的中位数
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
            step 1:
                nums3 = sourted(nums1 + nums2)
            step 2:
                compute the 中位数
        '''
        nums3 = sourted(nums1 + nums2)
        n = len(nums3)
        if n % 2 == 1:
            return float(nums3[n-1/2])
        else:
            return (nums3[n/2 - 1] + nums3[n/2])/2

