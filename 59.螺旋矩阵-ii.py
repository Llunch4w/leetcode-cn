#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        count, total = 0, n*n
        r, c = 0, 0
        
        while count < total:
            while c <= right and count < total:
                count += 1
                mat[top][c] = count
                c += 1
            top += 1
            r = top
            c = right
            while r <= bottom and count < total:
                count += 1
                mat[r][right] = count
                r += 1
            right -= 1
            c = right
            r = bottom
            while c >= left and count < total:
                count += 1
                mat[bottom][c] = count
                c -= 1
            bottom -= 1
            r = bottom
            c = left
            while r >= top and count < total:
                count += 1
                mat[r][left] = count
                r -= 1
            left += 1
            c = left
            r = top
        return mat
            
# @lc code=end

