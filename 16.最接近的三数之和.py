#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#
import sys

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        max_dis = sys.maxint
        res = None
        n = len(nums)
        nums.sort()
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            b, c = a+1, n-1
            while b < c:
                total = nums[a] + nums[b] + nums[c]
                if total == target:
                    return total
                else:
                    if abs(total-target) < max_dis:
                        max_dis = abs(total-target)
                        res = total
                    if total < target:
                        b += 1
                        while b < c and nums[b] == nums[b-1]:
                            b += 1
                    else:
                        c -= 1
                        while b < c and nums[c] == nums[c+1]:
                            c -= 1
        return res         
        
# @lc code=end

