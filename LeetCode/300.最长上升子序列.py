#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.35%)
# Likes:    374
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 92.8K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#
from typing import List

# @lc code=start


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划法，最差情况（输入序列有序）的时间复杂度为O(n^2)
        结果：
        24/24 cases passed (1196 ms)
        - Your runtime beats 33.13 % of python3 submissions
        - Your memory usage beats 99.54 % of python3 submissions (12.8 MB)
        """
        seq_len = []
        max_len = 0
        # 遍历输入数组的每个数字x，如果当前数字x比之前的数字y大，则x可以接在y后面组成新的上升子序列，
        # 新的子序列长度是以y结尾的最长子序列的长度+1。
        for i in range(len(nums)):
            x = nums[i]
            max_len_end_with_x = 1
            for j in range(i):
                y = nums[j]
                if y < x:
                    len_end_with_x = seq_len[j] + 1
                    if len_end_with_x > max_len_end_with_x:
                        max_len_end_with_x = len_end_with_x
            seq_len.append(max_len_end_with_x)
            if max_len_end_with_x > max_len:
                max_len = max_len_end_with_x
        return max_len

# @lc code=end