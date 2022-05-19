#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 等同于寻找第一个大于指定值的元素所在下标
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
        if left == len(nums)-1:
            return left + 1
        else:
            return left
# @lc code=end

