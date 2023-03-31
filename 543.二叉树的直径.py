#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_node_val = 0
        def find_max_path(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            max_left_len = find_max_path(node.left)
            max_right_len = find_max_path(node.right)
            node_val = max_left_len + max_right_len
            if node_val > self.max_node_val:
                self.max_node_val = node_val
            return max(max_left_len, max_right_len) + 1
        find_max_path(root)
        return self.max_node_val
        
# @lc code=end

