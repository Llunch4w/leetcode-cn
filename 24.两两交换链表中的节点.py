#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        solider = ListNode(0, head)
        pre_node = solider
        cur_node = head
        while cur_node is not None and cur_node.next is not None:
            next_node = cur_node.next
            cur_node.next = next_node.next
            next_node.next = cur_node
            pre_node.next = next_node
            pre_node = cur_node
            cur_node = pre_node.next
        return solider.next
# @lc code=end

