# usr/local/bin/python3.7
# _*_ config: utf-8 _*_
# Author: Felix
# FileName: 1_tow_sum.py

# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。

# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]

# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 题目：从一个数组中，找出相加等于目标值的数，并返回两数的下标，找出第一个即可；
        # 思路：爆破方式，轮询
        # 1.下标式轮询数组，次数-1
        # 2.子轮询数组，从父轮询后一位开始
        # 3.校验两数相加=目标值，并返回下标

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_sums(self, nums: List[int], target: int):

        # 题目：从一个数组中，找出相加等于目标值的数，并返回两数的下标，找出全部；
        # 思路：爆破方式，轮询
        # 1.下标式轮询数组，次数-1
        # 2.子轮询数组，从父轮询后一位开始
        # 3.校验两数相加=目标值，并返回下标

        sums = []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    sums.append([i, j])
        return sums

    def two_sum_hash(self, nums: List[int], target: int) -> List[int]:

        # 题目：从一个数组中，找出相加等于目标值的数，并返回两数的下标，找出第一个即可；
        # 思路：哈希表(推荐)
        # 1.枚举list，轮询列表
        # 2.计算目标值和当前数差
        # 3.检查hash表是否存在，存在返回结果，不存在存入hash表，数做key,下标为value

        hashtable = dict()
        # enumerate枚举list，返回下标和值
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[nums[i]] = i
        return []

    # def two_sums_hash(self, nums: List[int], target: int):
    #
    #     # 题目：从一个数组中，找出相加等于目标值的数，并返回两数的下标，找出全部；
    #     # 思路：哈希表
    #     # 1.枚举list，轮询列表
    #     # 2.计算目标值和当前数差
    #     # 3.检查hash表是否存在，存在则存入结果list，不存在存入hash表，数做key,下标为value
    #
    #     hashtable = dict()
    #     result = []
    #     for i, num in enumerate(nums):
    #         if target - num in hashtable:
    #             result.append([hashtable[target - num], i])
    #         hashtable[nums[i]] = i
    #
    #     return result


if __name__ == '__main__':
    nums = [10, 10, 10, 20, 9, 11]
    s = Solution()
    tar = s.two_sums(nums, 20)
    print(tar)


