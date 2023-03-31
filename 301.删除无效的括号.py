#
# @lc app=leetcode.cn id=301 lang=python
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l_remove, r_remove = 0, 0
        for c in s:
            if c == '(':
                l_remove += 1
            elif c == ')':
                if l_remove > 0:
                    l_remove -= 1
                else:
                    r_remove += 1
        res = []
        
        def is_valid(_str):
            cnt = 0
            for c in _str:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    if cnt > 0:
                        cnt -= 1
                    else:
                        return False
            return cnt == 0
                    
        def helper(sub_str, start, l_remove, r_remove):
            if l_remove == 0 and r_remove == 0:
                if is_valid(sub_str):
                    res.append(sub_str)
                return
            
            for i in range(start, len(sub_str)):
                if i > start and sub_str[i] == sub_str[i-1]:
                    continue
                if l_remove + r_remove > len(sub_str[i:]):
                    continue
                if l_remove > 0 and sub_str[i] == '(':
                    helper(sub_str[:i]+sub_str[i+1:], i, l_remove-1, r_remove)
                if r_remove > 0 and sub_str[i] == ')':
                    helper(sub_str[:i]+sub_str[i+1:], i, l_remove, r_remove-1)
        
        helper(s, 0, l_remove, r_remove)
        return res
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    s = "(a)())()"
    res = solution.removeInvalidParentheses(s)
    print(res)