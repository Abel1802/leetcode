#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: lizhu
# date: 2021-04-12
# email: lzblcu19@gmail.com
'''
    Leetcode-9 正则表达式匹配
'''


import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
            Step 1: s和p的第一个字符是否匹配

            Step 2: 处理p[1] == '*' 的情况：
                                            匹配0个或多个字符
            
            Step 3: 处理 '.' : 匹配一个字符


            这有一个使用python re模块的解法👍：
            def isMatch(self, s, p):
                s1 = re.compile(p).findall(s)
                if s1 == []:
                    return False;
                if s1[0] == s:
                    return True;
                else:
                    return False;
        '''
        # 结束条件
        if p:
            return not s
        
        first_match = (len(s) > 0) and p[0] in {s[0], '.'}        
        # 先处理 '*'
        if p[1] == '*' and len(p) >= 2:
            # 匹配0个 ｜ 多个
            return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
        # 处理 '.' 
        return first_match and self.isMatch(s[1:], p[1:])



if __name__ == '__main__':
    s = Solution()
    res = s.isMatch("aa", "a")
    print(res)