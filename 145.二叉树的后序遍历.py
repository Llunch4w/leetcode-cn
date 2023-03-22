#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        hash_dict = {}
        while stack:
            cur = stack[-1]
            if cur not in hash_dict:
                hash_dict[cur] = 1
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)  
            else:
                stack.pop()
                res.append(cur.val)  
        return res 
        
# @lc code=end

