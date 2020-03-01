#!/usr/bin/env python3
# author fool
# date 2020-03-01
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# using a violent method
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # length of string s
        L = len(s)
        max_sub = 0
        if L == 1:
            return max_sub + 1
        else:
            for i in range(L):
                # 因为这里是取当前子串 所以是 i to L+1
                for j in range(i,L+1):
                    # 取当前子串
                    tmp = s[i:j]
                    #print('tmp: {}; i: {}; j: {}'.format(tmp, i, j))
                    # 计算当前子串中不重复的字符个数
                    counts = {}
                    for str in tmp:
                        counts[str] = counts.get(str, 0 ) + 1
                    if len(counts) != len(tmp):
                        continue
                    else:
                        if len(tmp) > max_sub:
                            max_sub = len(tmp)

            return max_sub


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('au'))
    print(solution.lengthOfLongestSubstring(' '))
    print(solution.lengthOfLongestSubstring(''))


