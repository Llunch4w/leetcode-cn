#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        temp = []
        self.dfs(res, temp, 0, candidates, target)
        return res
    
    def dfs(self, res, temp, i, candidates, target):
        if target == 0:
            res.append(temp[:])
            return
        for j in range(i, len(candidates)):
            if candidates[j] <= target:
                temp.append(candidates[j])
                self.dfs(res, temp, j, candidates, target-candidates[j])
                temp.pop()
            else:
                break
# @lc code=end

