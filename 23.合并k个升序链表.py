#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import queue
        priority_queue = queue.PriorityQueue()
        # push every first node of each list into priority_queue
        for index, a_list in enumerate(lists):
            priority_queue.put(a_list.val, a_list.next)
            
        head = ListNode()
        tail = head
        # pick out the top item from queue and push the next item of its belong list into queue
        while not priority_queue.empty():
            node = priority_queue.get()
            next_node = node.next
            if next_node is not None:
                tail.next = node
                tail = tail.next
                priority_queue.put(next_node.val, next_node)
            
        return head.next
        
# @lc code=end

