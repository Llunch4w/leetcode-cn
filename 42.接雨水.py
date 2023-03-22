#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap_pointer(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    ans += (left_max) - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += (right_max) - height[right]
                right -= 1
        return ans
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                cur = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                w = i - left - 1
                h = min(height[i], height[left]) - height[cur]
                ans += h * w
            stack.append(i)
        return ans
        
# @lc code=end

