#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(len(s)):
            dp[i][i]= True
        max_len = 1
        start = 0
        for length in range(2, n+1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    continue
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
        return s[start: start+max_len]
    
# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.longestPalindrome("aacabdkacaa"))
                
# @lc code=end

