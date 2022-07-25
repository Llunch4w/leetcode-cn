#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        soilder = ListNode(0, head)
        pre_node = soilder

        while pre_node.next is not None:
            start = pre_node.next
            # print(start.val)
            end = start
            is_reverse = True
            for _ in range(k-1):
                end = end.next
                if end is None:
                    break
            if end is None:
                is_reverse = False
                break
            if not is_reverse:
                break
            
            tail_next = end.next
            end.next = None
            new_start, new_end = self.sub_reverse(start)
            # print(new_head.val, new_tail.val)
            pre_node.next = new_start
            new_end.next = tail_next
            pre_node = new_end

        return soilder.next
    
    def sub_reverse(self, start):
        """reverse the list
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        soilder = ListNode(0, start)
        cur_node = start.next
        pre_node = start
        while cur_node is not None:
            next_node = cur_node.next
            pre_node.next = next_node
            cur_node.next = soilder.next
            soilder.next = cur_node
            cur_node = pre_node.next
        tail_node = pre_node
        return soilder.next, tail_node
        
# @lc code=end

