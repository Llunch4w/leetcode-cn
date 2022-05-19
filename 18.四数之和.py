#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums.sort()
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c, d = b+1, n-1
                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                    else:
                        if total > target:
                            d -= 1
                            while c < d and nums[d] == nums[d+1]:
                                d -= 1
                        else:
                            c += 1
                            while c < d and nums[c] == nums[c-1]:
                                c += 1
        return res    
# @lc code=end

