#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s = x ^ y
        ret = 0
        while s:
            s = s & (s-1)
            ret += 1
        return ret
# @lc code=end

