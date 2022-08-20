#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        stack = [root]
        is_left = True
        while not len(stack) == 0:
            new_stack = []
            level_values = []
            if not is_left:
                for i in range(len(stack)-1, -1, -1):
                    level_values.append(stack[i].val)
                res.append(level_values)
                is_left = True
            else:
                for i in range(len(stack)):
                    level_values.append(stack[i].val)
                res.append(level_values)
                is_left = False
                
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return res

        
# @lc code=end

