#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        res = []
        if not root:
            return root
        p = root
        stack = [p]
        while stack:
            cur = stack.pop()
            res.append(cur)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        new_root = res[0]
        p = new_root
        for i in range(1, len(res)):
            p.right = res[i]
            p.left = None
            p = p.right
        p.left = None
        p.right = None
        return new_root
        
# @lc code=end

