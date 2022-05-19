#
# @lc app=leetcode.cn id=41 lang=python
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        # print(nums)
        for i in range(n):
            if abs(nums[i]) <= n:
                loc = abs(nums[i])-1
                nums[loc] = -abs(nums[loc])
        # print(nums)
                
        for i in range(n):
            if nums[i] >= 0:
                return i+1
        
        return n+1
# @lc code=end

