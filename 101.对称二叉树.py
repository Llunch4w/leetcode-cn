#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def dfs(left, right):
            # 均为空节点
            if not (left or right):
                return True
            # 有且仅有一个节点为空
            if not (left and right):
                return False
            # 节点均不为空，但值不相等
            if left.val != right.val:
                return False
            if dfs(left.left, right.right) and dfs(left.right, right.left):
                return True
            return False
        return dfs(root.left, root.right)
        
# @lc code=end

