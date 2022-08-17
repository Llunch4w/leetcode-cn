#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = ListNode()
        p = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                q = list1
                p.next = q
                list1 = list1.next
                q.next = None
            else:
                q = list2
                p.next = q
                list2 = list2.next
                q.next = None
            p = p.next
        if list1 is not None:
            p.next = list1
        elif list2 is not None:
            p.next = list2
        return new_head.next
            
# @lc code=end

