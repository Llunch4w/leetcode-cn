#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            target = -nums[a]
            c = n - 1
            for b in range(a+1, n):
                if b > a+1 and nums[b]==nums[b-1]:
                    continue
                while b < c and nums[b] + nums[c] > target:
                    c -= 1
                if b == c:
                    break
                if nums[b] + nums[c] == target:
                    res.append([nums[a], nums[b], nums[c]])
        return res
# @lc code=end

