#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # boundary
        if len(s) < 2:
            return len(s)
        # slide window
        window_dict = {}
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            c = s[right]
            if c not in window_dict:
                window_dict[c] = right
            elif window_dict[c] < left:
                window_dict[c] = right
            else:
                if right - left > max_len:
                    max_len = right - left
                left = window_dict[c] + 1
                window_dict[c] = right
            # print(c,  max_len)
            right += 1
        if right - left > max_len:
            max_len = right - left
        return max_len
        
# @lc code=end

