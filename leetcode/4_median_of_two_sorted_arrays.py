# usr/local/bin/python3.7
# -*-coding: utf-8 -*-
# Author: Felix
# FileName: 4_median_of_two_sorted_arrays.py

# 4. 寻找两个正序数组的中位数
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 示例 3：
#
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
# 示例 4：
#
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
# 示例 5：
#
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
# 提示：
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        """
        中位数概念：是指一组数据从小到大排列，位于中间的那个数。可以是一个（数据为奇数），也可以是2个的平均（数据为偶数）
        步骤：
        1.合并两个列表
        2.正序排序
        3.校验奇数和偶数计算中位数
        """

        nums1.extend(nums2)
        nums1.sort()

        le = len(nums1)

        if le % 2 == 0:
            middle = (nums1[le//2 - 1] + nums1[le//2]) / 2
        else:
            middle = float(nums1[le//2])
        return middle


if __name__ == '__main__':

    s = Solution()
    num1 = []
    num2 = [1]
    middle = s.findMedianSortedArrays(num1, num2)
    print(middle)

