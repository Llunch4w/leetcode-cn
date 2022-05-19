#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        for i, v in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i+v)
        return True
# @lc code=end

