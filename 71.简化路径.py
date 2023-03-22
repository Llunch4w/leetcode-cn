#
# @lc app=leetcode.cn id=71 lang=python
#
# [71] 简化路径
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        item_list = path.split("/")
        stack = []
        for item in item_list:
            if len(item) == 0:
                continue
            elif item == ".":
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)
    
# @lc code=end

