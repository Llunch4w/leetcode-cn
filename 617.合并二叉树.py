#
# @lc app=leetcode.cn id=617 lang=python
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def merged(root1, root2):
            if not root1:
                return root2
            if not root2:
                return root1
            
            merge_root = TreeNode(root1.val + root2.val)
            merge_root.left = merged(root1.left, root2.left)
            merge_root.right = merged(root1.right, root2.right)
            return merge_root
        return merged(root1, root2)
    
# @lc code=end

