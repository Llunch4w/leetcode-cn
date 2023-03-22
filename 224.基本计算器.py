#
# @lc app=leetcode.cn id=224 lang=python
#
# [224] 基本计算器
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        s = s.replace("(-", "(0-")
        if s[0] == "-":
            s = "0" + s
        op_level = {"(":0, "+": 1, "-": 1, "*":2, "/": 2}
        num_stack, op_stack = [], []
        i = 0
        while i < len(s):
            c = s[i]
            if c in ["+", "-", "*", "/"]:
                if op_stack and op_level[op_stack[-1]] >= op_level[c]:
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    op = op_stack.pop()
                    num = self.simple_cal(num1, num2, op)
                    num_stack.append(num)
                    op_stack.append(c)
                else:
                    op_stack.append(c)
            elif c == "(":
                op_stack.append(c)
            elif c == ")":
                while op_stack[-1] != "(":
                    op = op_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    num = self.simple_cal(num1, num2, op)
                    num_stack.append(num)
                op_stack.pop()
            else:
                num = 0
                while i< len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                num_stack.append(num)
                i -= 1
            i += 1
            
        while op_stack:
            op = op_stack.pop()
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            num = self.simple_cal(num1, num2, op)
            num_stack.append(num)
        return num_stack[-1]
                    
    def simple_cal(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    s = "-2+1"
    print(solution.calculate(s))