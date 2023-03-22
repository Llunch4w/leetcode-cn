#
# @lc app=leetcode.cn id=150 lang=python
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num_stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                num_stack.append(int(token))
            else:
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                if token == "+":
                    num_stack.append(num1+num2)
                elif token == "-":
                    num_stack.append(num1-num2)
                elif token == "/":
                    num_stack.append(int(num1/num2))
                elif token == "*":
                    num_stack.append(num1*num2)
        return num_stack[-1]
# @lc code=end

if __name__ == "__main__":
    test_case = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    solution = Solution()
    print(solution.evalRPN(test_case))

