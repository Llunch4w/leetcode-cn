#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        num_sum = sum(nums)
        if num_sum & 1:
            return False
        target = num_sum // 2
        nums.sort()
        # # dp[i][j] 代表是否能从 nums[0:i+1]中选择k个元素，使和为j
        # dp = [[False]*(target+1) for _ in range(n)]
        # # 初始条件, 任意dp[i][0]为True，因为可以不选
        # for i in range(n):
        #     dp[i][0] = True
        # # 初始条件，dp[0][nums[0]] = True
        # dp[0][nums[0]] = True
        # '''
        # 对于第i个物品, 若 j > nums[i]
        # dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]
        # 若 j < nums[i]
        # dp[i][j] = dp[i-1][j]
        # '''
        # for i in range(1, n):
        #     for j in range(target+1):
        #         if nums[i] < j:
        #             dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # return dp[n-1][target]
    
        '''空间优化'''
        dp = [True] + [False] * (target+1)
        for i in range(1, n):
            for j in range(target, nums[i]-1, -1):
                dp[j] |= dp[j-nums[i]]
        return dp[target]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    nums = [3,3,3,4,5]
    res = solution.canPartition(nums)
    print(res)
