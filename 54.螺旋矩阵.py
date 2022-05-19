#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        total = (bottom+1) * (right+1)
        count = 0
        res = []
        
        r, c = 0, 0
        while count < total: 
            while c <= right and count < total:
                res.append(matrix[top][c])
                count += 1
                c += 1
            top += 1
            r = top
            c = right
            while r <= bottom and count < total:
                res.append(matrix[r][right])
                count += 1
                r += 1
            right -= 1
            c = right
            r = bottom
            while c >= left and count < total:
                res.append(matrix[bottom][c])
                count += 1
                c -= 1
            bottom -= 1
            r = bottom
            c = left
            while r >= top and count < total:
                res.append(matrix[r][left])
                count += 1
                r -= 1
            left += 1
            c = left
            r = top
        return res
            
# @lc code=end

