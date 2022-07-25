#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        priority_queue = []
        # push every first node of each list into priority_queue
        for index in range(len(lists)):
            if lists[index]:
                heapq.heappush(priority_queue, (lists[index].val, index))
            
        head = ListNode()
        tail = head
        # pick out the top item from queue and push the next item of its belong list into queue
        while priority_queue:
            val, idx = heapq.heappop(priority_queue)
            # print("val=" + str(val))
            new_node = ListNode(val)
            tail.next = new_node
            tail = new_node
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(priority_queue, (lists[idx].val, idx))
            
        return head.next
        
# @lc code=end

