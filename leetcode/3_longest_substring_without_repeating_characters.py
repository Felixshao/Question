# usr/local/bin/python3.7
# -*-coding: utf-8 -*-
# Author: Felix
# FileName: 3_longest_substring_without_repeating_characters.py

# 3. 无重复字符的最长子串
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
#     请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
# 示例 4:
#
# 输入: s = ""
# 输出: 0
#
# 提示：
#
# 0 <= s.length <= 5 * 104
# s由英文字母、数字、符号和空格组成

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        思路：
        1.将字符串变更为列表，设置一个空结果列表
        2.从头开始轮询， 以当前节点放入列表，开始逐个校验是否相等，不相等方法列表继续
        3.得出单次轮询结果对比结果列表，数量大于则取代
        4.重复轮询
        """

        le = len(s)
        s_list = list(s)
        num = []    # 设置一个空结果列表

        # 从头开始轮询字符串
        for i in range(le):
            chrid = [s_list[i]]
            # 对比是否相等
            for j in range(i+1, len(s)):
                if s_list[j] in chrid:
                    break
                else:
                    chrid.append(s_list[j])
            # 对比新旧结果子串
            if len(chrid) > len(num):
                num = chrid.copy()
            # 减少轮询次数
            if (len(num) >= le/2) and (i >= le/2):
                break

        return len(num)

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
                print(s[i-1], end=' ')
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
            print(i, rk, occ, ans)
        return ans


if __name__ == '__main__':

    s = Solution()
    st = 'abcabcd'
    n = s.lengthOfLongestSubstring2(st)
    print(n)
    b = set()
    for i in st:
        b.add(i)
    b.remove('a')
    print(b)


