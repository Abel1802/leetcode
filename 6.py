#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
    Leetcode-6 z字形变换
'''
import numpy as np


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''

            Step 1: 可以用一个列表表示，每一个元素是一个字符串；
                    （而我的思维使用两个列表，每个元素是一个字符，导致最后无法逆序）

            Step 2: 只对s遍历，i用flag更新
        '''
        if numRows < 2: return s
        res = ["" for _ in range(numRows)] # 每一行是一个字符串
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag # 转折处的条件
            i += flag
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    s.convert('PAYPALISHIRING', 4)
