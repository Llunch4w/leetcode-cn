#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = {}
        for _str in strs:
            sorted_str = "".join(sorted(_str))
            if sorted_str in hash_map:
                str_list = hash_map.get(sorted_str)
                str_list.append(_str)
            else:
                hash_map[sorted_str] = [_str]
        return list(hash_map.values())
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))

