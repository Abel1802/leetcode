#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: lizhu
# date: 2021-04-11
# email: lzblcu19@gmail.com
'''
    Leetcode-8 字符串转整数
'''

import re

class Solution:
    def myAtoi(self, s: str) -> int:
        '''
            Key: 使用正则来处理字符串！！！
        '''
        INT_MAX = 2147483647    
        INT_MIN = -2147483648
        s = s.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(s)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值


if __name__ == '__main__':
    s = Solution()
    s.myAtoi("4193 with words")