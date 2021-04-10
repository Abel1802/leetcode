#!/usr/bin/env python3
# author fool
# date 2020-03-01
'''
    Leetcode-3 无重复字符的最长子串
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            想到hash，但是不知道怎么控制, 例如 " a b c a b c b b "

            难点一：找最大子串，所以一定会有两个关键值：
                                                第一个都容易想到，就是遍历原字符串；（其实是子串的末尾下标）
                                                第二个容易忽略，控制子串的起始起始下标（用一个变量控制）

            难点二：如何更新子串的起始下标k: 用hash记录每个字母c的下标：
                                        if c in dict 且 上一次的c的下标 > 子串起始下标k： (保证了在k前面的字符的重复也被算进去) 例如"tmmzuxt"
                                            更新k, 
                                            更新hash, 
                                        else:
                                            dict[c] = i
                                            res = max(res, i-k)
        '''
        res, c_dict = 0, {}
        k = -1 # 用于控制子串的起始点（从-1的后面开始，也就是i - k的子串长度， i是末尾点）
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res
        