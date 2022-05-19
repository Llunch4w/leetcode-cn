import sys
#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_min = -10001
        n = len(nums)
        # i: slot to fill, j: pointer
        i, j = 0, 0
        while j < n:
            if nums[j] > cur_min:
                nums[i] = nums[j]
                cur_min = nums[j]
                i += 1
            j += 1
        return i
                       
# @lc code=end

