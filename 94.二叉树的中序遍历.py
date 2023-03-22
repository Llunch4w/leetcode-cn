#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        p = root
        stack = [p]
        is_right = True
        while stack:
            cur = stack[-1]
            while cur.left and is_right:
                stack.append(cur.left)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            is_right = False
            if cur.right:
                stack.append(cur.right)
                is_right = True
        return res
            
# @lc code=end

# if __name__ == "__main__":
#     solution = Solution()
#     root = TreeNode(1)
#     root.left = TreeNode(4)
#     root.left.left = TreeNode(5)
#     root.left.right = TreeNode(6)
#     root.right = TreeNode(2)
#     root.right.left = TreeNode(3)
#     print(solution.inorderTraversal(root))