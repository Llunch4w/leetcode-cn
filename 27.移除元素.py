#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                if left != right:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return left
# @lc code=end

