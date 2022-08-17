#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            level_ans = [node.val for node in stack]
            res.append(level_ans)
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return res           
                           
# @lc code=end

