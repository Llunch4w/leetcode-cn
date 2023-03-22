#
# @lc app=leetcode.cn id=316 lang=python
#
# [316] 去除重复字母
#
import collections

# @lc code=start
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        stack = []
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and counter[stack[-1]]:
                    stack.pop()
                stack.append(c)
            counter[c] -= 1
        return "".join(stack)
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    s = "cbacdcbc"
    print(solution.removeDuplicateLetters(s))