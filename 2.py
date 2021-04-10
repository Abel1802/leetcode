#!/usr/bin/env python3
# author lizhu
# date 2020-02-29
# update 2021-04-10
'''
    leetcode-2 addTwoNumbers
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
            第一：首先逆序不知如何解决
                其实，先逆序求和，得到结果后在逆序回来和一开始正序求和的结果一样！！！

            第二：两个列表的遍历有问题
                先更新next
                再更新val
        '''
        carry = 0
        ret = ListNode()
        cur = ret
        while l1 or l2 or carry:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            if carry:
                num += carry
                carry -= 1
            carry, num = divmod(num, 10)
            cur.next = ListNode(num)
            cur = cur.next

        return ret.next     #   ret.val = 0
