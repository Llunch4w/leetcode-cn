#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []
        # 单调递减栈
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()
        return val

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.top())
    print(min_stack.getMin())

