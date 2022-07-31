#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        pre, cur = head, head.next
        pre.next = None
        while cur is not None:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre   
        
# @lc code=end

