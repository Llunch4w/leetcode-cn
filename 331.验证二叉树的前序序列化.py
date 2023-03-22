#
# @lc app=leetcode.cn id=331 lang=python
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        order_list = preorder.split(",")
        stack = []
        for c in order_list:
            stack.append(c)
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
                for _ in range(3):
                    stack.pop()
                stack.append("#")
        if len(stack) == 1 and stack[0] == "#":
            return True
        else:
            return False
        
# @lc code=end

