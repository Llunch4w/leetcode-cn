#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        chose[i]: 在i节点选择i的最大值
        unchose[i]: 在i节点不选择i的最大值
        '''
        chose = {None: 0}
        unchose = {None: 0}
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            chose[node] = node.val + unchose[node.left] + unchose[node.right]
            unchose[node] = max(chose[node.left], unchose[node.left]) + max(chose[node.right], unchose[node.right]) 
        
        dfs(root)
        return max(chose[root], unchose[root])
        
# @lc code=end

