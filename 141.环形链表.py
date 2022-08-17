#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next is None or head.next.next is None:
            return False
        fast, slow = head.next.next, head.next
        while fast is not None:
            if fast == slow:
                return True
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        
        
# @lc code=end

