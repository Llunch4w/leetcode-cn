#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inorder_index = {order: i for i, order in enumerate(inorder)}
        def dfs(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            node = TreeNode(preorder[pre_left])
            in_index = inorder_index[preorder[pre_left]]
            left_part_num = (in_index-1) - in_left + 1
            # right_part_num = in_right - (in_index + 1) + 1
            node.left = dfs(pre_left+1, pre_left+left_part_num, in_left, in_index-1)
            node.right = dfs(pre_left+left_part_num+1, pre_right, in_index+1, in_right)
            return node
        n = len(preorder)
        return dfs(0, n-1, 0, n-1)
        
# @lc code=end

