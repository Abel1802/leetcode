#!usr/bin/env python3
# author fool
# date 2020-03-02
'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findMedian(l):
            median = 0
            L = len(l)
            if L == 0:
                print('list is null')
            else:
                if L % 2 == 0:
                    median = (l[L/2 - 1] + l[L/2]) / 2
                else:
                    median = l[int((L - 1) / 2)]
            return median

        index = 0
        len1 = len(nums1)
        len2 = len(nums2)
        nums3 = []
        # 5种情况 对2个有序表合并
        if nums2[len2 -1] < nums1[0]:
            nums3 = nums2 + nums1
            print(1)
        elif nums2[0] < nums1[0] and nums2[len2 -1] > nums1[0]:
            print(2)
        elif nums2[0] > nums1[0] and nums2[len2 -1] < nums1[len1 - 1]:
            print(3)
        elif nums2[0] < nums1[len1 -1] and nums2[len2 -1] > nums1[len1 -1]:
            print(4)
        elif nums2[0] > nums1[len1 -1]:
            nums3 = nums1 + nums2
            print(5)
        else:
            pass
        return findMedian(nums3)


if __name__ == '__main__':
    solution = Solution()
    median = solution.findMedianSortedArrays([0, 1], [2, 3, 4])
    print('median: ', median)