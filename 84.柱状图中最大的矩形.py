#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 维护单调递增栈
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                area = heights[cur] * ((right-1) - (left+1) + 1)
                if area > max_area:
                    max_area = area
            stack.append(i)
        while stack:
            cur = stack.pop()
            left = -1 if not stack else stack[-1]
            right = len(heights)
            area = heights[cur] * ((right-1) - (left+1) + 1)
            if area > max_area:
                max_area = area
        return max_area
# @lc code=end

