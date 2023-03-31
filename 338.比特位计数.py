#
# @lc app=leetcode.cn id=338 lang=python
#
# [338] 比特位计数
#

# @lc code=start
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        bits = [0] * (n+1)
        for i in range(1, n+1):
            # i >> 1 为i右移丢弃最低位
            # i & 1 判断最后一位是否为1
            bits[i] = bits[i >> 1] + (i & 1)
        return bits
# @lc code=end

