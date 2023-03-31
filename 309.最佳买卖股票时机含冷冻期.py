#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        '''三种股票状态
        dp[i][0]: 第i天持有股票
        dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
        dp[i][1]: 第i天不持有股票，且处于冷静期
        dp[i][1] = dp[i-1][0]+prices[i]
        dp[i][2]: 第i天不持有股票，且不处于冷静期
        dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        '''
        state0, state1, state2 = -prices[0], 0, 0
        for i in range(1, n):
            old_state2 = state2
            state2 = max(state1, state2)
            state1 = state0+prices[i]
            state0 = max(state0, old_state2-prices[i])
        return max(state1, state2)      
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    prices = [1,2,3,0,2]
    res = solution.maxProfit(prices)
    print(res)
