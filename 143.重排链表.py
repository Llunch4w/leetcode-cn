#
# @lc app=leetcode.cn id=143 lang=python
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        left_stack = []
        p = head
        n = 0
        while p:
            left_stack.append(p)
            p = p.next
            n += 1
        right_stack = []
        for _ in range(n//2):
            right_stack.append(left_stack.pop())
        if n%2 != 0:
            last_node = left_stack.pop()
            last_node.next = None
        else:
            last_node = None
        for _ in range(n//2):
            left_node = left_stack.pop()
            right_node = right_stack.pop()
            left_node.next = right_node
            right_node.next = last_node
            last_node = left_node
        return last_node
        
# @lc code=end

# if __name__ == "__main__":
#     solution = Solution()
#     arr = [1, 2, 3, 4, 5]
#     head = ListNode()
#     p = head
#     for item in arr:
#         p.next = ListNode(item)
#         p = p.next
#     new_head = solution.reorderList(head.next)
#     while new_head:
#         print(new_head.val)
#         new_head = new_head.next