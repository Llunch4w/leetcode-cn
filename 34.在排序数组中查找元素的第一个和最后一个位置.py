#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_bound = self.searchLeft(nums, target)
        right_bound = self.searchRight(nums, target)
        return [left_bound, right_bound]
    
    def searchLeft(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def searchRight(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid + 1
        return -1
# @lc code=end

