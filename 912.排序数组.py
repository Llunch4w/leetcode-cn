#
# @lc app=leetcode.cn id=912 lang=python
#
# [912] 排序数组
#

# @lc code=start
import random

class Solution(object):
    def quickSort(self, left, right):
        if left >= right:
            return
        index = random.randint(left, right)
        self.nums[index], self.nums[right] = self.nums[right], self.nums[index]
        i, j = left-1, left
        while j < right:
            if self.nums[j] < self.nums[right]:
                i += 1
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            j += 1
        i += 1
        self.nums[i], self.nums[right] = self.nums[right], self.nums[i]
        self.quickSort(left, i-1)
        self.quickSort(i+1, right)
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        self.quickSort(0, len(nums)-1)
        return self.nums
       
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [5,2,3,1]
#     print(solution.sortArray(nums))
# @lc code=end

