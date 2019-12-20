#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (59.01%)
# Likes:    210
# Dislikes: 0
# Total Accepted:    29.5K
# Total Submissions: 49.9K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 
# 示例 1:
# 
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 
# 
# 示例 2:
# 
# 输入: nums = [1], k = 1
# 输出: [1]
# 
# 说明：
# 
# 
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 
# 
#

"""
思路：
可将这个问题分解为2个问题：
1) 统计每个整数出现的次数;
2) 获取前k个最大的值。

第一步，确定每个整数出现的次数，可以简单地用一个字典对象维护每个值出现的次数。
遍历数组，每个数字出现时就给它的计数+1。

第二步，
"""
from typing import List
from collections import 


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 第一步：整数的出现次数
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        # 第二步：构建大根堆
        heap = BigRootHeap()
        for n, count in counts.items():
            node = Node(count, n)
            heap.push(node)

        # 第三步：依次取出前k个元素
        result = [heap.pop().value for _ in range(k)]
        return result


class BigRootHeap:


# @lc code=end

