#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        count_s = [0] * 26
        count_p = [0] * 26
        a_ascii = ord('a')
        for i in range(len(p)):
            p_index = ord(p[i]) - a_ascii
            s_index = ord(s[i]) - a_ascii
            count_s[s_index] += 1
            count_p[p_index] += 1
            
        answer = []
        if count_s == count_p:
            answer.append(0)
            
        for i in range(len(s)-len(p)):
            old_char_index = ord(s[i]) - a_ascii
            new_char_index = ord(s[i+len(p)]) - a_ascii
            count_s[new_char_index] += 1
            count_s[old_char_index] -= 1
            if count_s == count_p:
                answer.append(i+1)
        return answer
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    s = "abab"
    p = "ab"
    answer = solution.findAnagrams(s, p)
    print(answer)
