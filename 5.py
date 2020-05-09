#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
    leedcode(05):
    最长回文子串:
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

        示例 1：
        输入: "babad"
        输出: "bab"
        注意: "aba" 也是一个有效答案。

        示例 2：
        输入: "cbbd"
        输出: "bb"
'''
# 暴力法
class Solution(object):
    def __init__(self):
        super(Solution, self).__init__()
    def isPalindrome(self, s):
        '''
        Parameters:
             s: a string
        Return:
            boolean: the string is palindrome or not
        '''
        len_str = len(s)
        for i in range(int(len_str/2)):
            if s[i] != s[len_str - i - 1]:
                return False
        return True

    def longestPalindrome(self, s):
        """
        parameters:
            s: input (a string)
        return : the longest palindrome of the string
        """
        # Step 1: for loop: i from 0 to (len - 1)
        # Step 2: for loop: j from i to (len - 1)
        len_str = len(s)
        max_str = 0
        for i in range(len_str):
            for j in range(i,len_str+1):
                test_str = s[i:j]
                print(i, j, test_str)
                if self.isPalindrome(test_str) and len(test_str) > max_str:
                    ans = test_str
                    max_str = max(len(test_str), max_str)
        return ans



if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    out = solution.longestPalindrome(s)
    print("The longest Palindrome of '{}' is : {}".format(s, out))