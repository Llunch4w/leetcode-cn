#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i-j < 2 or dp[j+1][i-1]):
                    ans += 1
                    dp[j][i] = True
        return ans
# @lc code=end

