#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_border = 0
        # 上左边界赋值
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j]:
                max_border = 1
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0]:
                max_border = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_border = max(dp[i][j], max_border)
        return max_border * max_border
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    matrix = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
    res = solution.maximalSquare(matrix)
    print(res)

