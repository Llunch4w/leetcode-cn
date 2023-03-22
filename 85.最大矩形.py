#
# @lc app=leetcode.cn id=85 lang=python
#
# [85] 最大矩形
#

# @lc code=start
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area = 0
        for i in range(len(matrix)):
            heights = self.count_height(matrix[0: i+1])
            area = self.count_max_area(heights)
            if max_area < area:
                max_area = area
        return max_area
        
    def count_height(self, matrix):
        heights = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
        return heights
    
    def count_max_area(self, heights):
        # 单调递增栈
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                area = heights[cur] * ((right-1) - (left+1) + 1)
                if max_area < area:
                    max_area = area
            stack.append(i)
        while stack:
            cur = stack.pop()
            left = -1 if not stack else stack[-1]
            right = len(heights)
            area = heights[cur] * ((right-1) - (left+1) + 1)
            if max_area < area:
                max_area = area
        return max_area
# @lc code=end

