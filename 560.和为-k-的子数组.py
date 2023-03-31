#
# @lc app=leetcode.cn id=560 lang=python
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution(object):
    '''
    前缀和 dp + hashmap
    (dp[i] - dp[j-1] == k) => [i, j] 是和为k的连续子数组
    '''
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        total_sum = 0
        preffix_sum_map = {0: 1}
        for num in nums:
            total_sum += num
            ans += preffix_sum_map.get(total_sum-k, 0)
            preffix_sum_map[total_sum] = preffix_sum_map.get(total_sum, 0) + 1
        return ans
            
            
# @lc code=end

