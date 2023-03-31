#
# @lc app=leetcode.cn id=437 lang=python
#
# [437] 路径总和 III
#
import collections
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        preffix = {}
        preffix[0] = 1
        def dfs(node, curr):
            '''curr代表node父节点的前缀和'''
            if not node:
                return 0
            ret = 0
            curr += node.val
            ret += preffix.get(curr-targetSum, 0)
            preffix[curr] = preffix.get(curr, 0) + 1
            ret += dfs(node.left, curr)
            ret += dfs(node.right, curr)
            preffix[curr] -= 1
            curr -= node.val
            return ret
        
        return dfs(root, 0)    
        
# @lc code=end

