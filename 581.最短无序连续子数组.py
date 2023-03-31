#
# @lc app=leetcode.cn id=581 lang=python
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution(object):
    '''
    数组分为3部分: sa, sb, sc
    需要满足：
    (1) sa 的最大值 <= [sb, sc] 中的最小值
    (2) sc 的最小值 >= [sa, sb] 中的最大值
    
    从左往右找比当前最大值小的最右最远坐标
    从右往左找比当前最小值大的最左最远坐标
    
    [2,6,4,8,10,9,15]
    最大值: 10 最右: 9_index
    最小值: 4 最左: 6_index
    
    [1,2,3,4]
    最大值: 4 最右：-1
    最小值: 1 最左：-1
    
    [1,3,2,2,2]
    最大值: 3 最右: last_2_index
    最小值: 2 最左: 3_index
    
    [1,2,3,3,3]
    最大值: 3 最右: -1
    最小值: 1 最左: -1
    '''
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_n = float('-inf')
        min_n = float('inf')
        left, right = -1, -1
        for i in range(n):
            if nums[i] >= max_n:
                max_n = nums[i]
            else:
                right = i
            
            if nums[n-1-i] <= min_n:
                min_n = nums[n-1-i]
            else:
                left = n-1-i
        return 0 if right ==-1 else right - left + 1
    
# @lc code=end

