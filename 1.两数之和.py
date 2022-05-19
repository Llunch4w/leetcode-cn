#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # {num: index}
        recorded = {}
        for i, num in enumerate(nums):
            if num in recorded:
                return [i, recorded[num]]
            else:
                recorded[target-num] = i
        return [-1, -1]
    
# @lc code=end

