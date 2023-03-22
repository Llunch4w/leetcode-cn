#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_types = ["(", "{", "["]
        right_types = [")", "}", "]"]
        left_dict, right_dict = {}, {}
        
        for i in range(3):
            left_dict[left_types[i]] = i
            right_dict[right_types[i]] = i
            
        stack = []
        for c in s:
            if c in left_dict:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                top = stack[-1]
                stack = stack[:-1]
                if left_dict[top] != right_dict[c]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                
# @lc code=end

