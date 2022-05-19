#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子数组和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        res = 0
        
        for _, item in enumerate(nums):
            res += item
            if res > max_sum:
                max_sum = res
            if res < 0:
                res = 0
        return max_sum
# @lc code=end

