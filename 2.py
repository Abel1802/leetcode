#!/usr/bin/env python3
# author fool; date 2020-02-29
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# python list version （the entitle request ListNode type）
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = []
        len1 = len(l1)
        len2 = len(l2)
        # list1 与list2 等长
        if len1 == len2:
            # 记录该位是否逢十进一
            flag = 0
            for i in range(len1):
                tmp = l1[i] + l2[i]
                if tmp > 9:
                    tmp = tmp - 10
                    l3.append(tmp + flag)
                    flag = 1
                else:
                    l3.append(tmp + flag)
                    flag = 0
            # 最后一位是否进一
            if flag == 1:
                l3.append(1)
        # list1 长度小于 list2
        elif len1 < len2:
            flag = 0
            index = 0
            # 在list1长度和list2相等的情况
            for i in range(len1):
                index += 1
                tmp = l1[i] + l2[i]
                if tmp > 9:
                    tmp = tmp - 10
                    l3.append(tmp + flag)
                    flag = 1
                else:
                    l3.append(tmp + flag)
                    flag = 0
            # 在list2剩余的长度下的情况
            for j in range(index, len2):
                tmp = l2[j] + flag
                if tmp > 9:
                    tmp = tmp - 10
                    l3.append(tmp )
                    flag = 1
                else:
                    l3.append(tmp)
                    flag = 0
            # 最后一位是否进一
            if flag == 1:
                l3.append(1)
        # list1 长度大于 list2
        elif len1 > len2:
            flag = 0
            index = 0
            # 在list1长度和list2相等的情况
            for i in range(len2):
                index += 1
                tmp = l1[i] + l2[i]
                if tmp > 9:
                    tmp = tmp - 10
                    l3.append(tmp + flag)
                    flag = 1
                else:
                    l3.append(tmp + flag)
                    flag = 0
            # 在list1剩下的长度情况
            for j in range(index, len1):
                tmp = l1[j] + flag
                if tmp > 9:
                    tmp = tmp - 10
                    l3.append(tmp)
                    flag = 1
                else:
                    l3.append(tmp)
                    flag = 0
            # 最后一位是否进一
            if flag == 1:
                l3.append(1)
        return l3

if __name__ == '__main__':
    print('Using python list type!')
    solution = Solution()
    print(solution.addTwoNumbers([9, 8, 9], [2, 5]))

