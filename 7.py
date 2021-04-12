#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: lizhu
# date: 2021-04-11
# email: lzblcu19@gmail.com
'''
    Leetcode-7 整数反转
'''


class Solution:
    def reverse(self, x: int) -> int:
        '''
            Step 1: int -> str

            Step 2: 去掉末尾为0的字符，逆序字符串 -> int
                    Note:这里有一个陷阱，去掉末尾的0，不能直接str.replace('0', ''), 例如901000

                    Note!!!: 实际上不需要去掉开头为0的字符，因为转化为int时，就已经去掉了

                    还有！！！，判断范围是转化后的res,不是刚开始的x
        '''
        
        if x > 0:
            res = self.reverse_Pint(x)
        elif x < 0:
            res = -self.reverse_Pint(-x)
        else:
            res = 0
        
        return res if -pow(2, 31) <= res <= pow(2, 31) -1 else 0
        
    def reverse_Pint(self, x: int) -> int:
        x_str = str(x)
        x_str_rev = x_str[::-1]
        ''' 下面这一段去掉开头为0的字符，不需要！！！'''
        # for i,c in enumerate(x_str_rev):
        #     if c != '0':
        #         idx = i
        #         break
        #     else:
        #         print('c = {}, i = {}'.format(c, i))
        #         idx = i + 1
        return int(x_str_rev)