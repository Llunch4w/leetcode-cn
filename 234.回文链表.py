#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        n = 0
        p = head
        while p:
            stack.append(p.val)
            n += 1
            p = p.next
        p = head
        for _ in range(n//2):
            if stack.pop() != p.val:
                return False
            p = p.next
        return True
        
# @lc code=end

