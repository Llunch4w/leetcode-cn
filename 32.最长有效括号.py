#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len
                    
# @lc code=end

# if __name__ == "__main__":
#     solution = Solution()
#     s = "(()))())("
#     print(solution.longestValidParentheses(s))