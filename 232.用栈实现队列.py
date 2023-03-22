#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.push_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.push_stack and not self.pop_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

