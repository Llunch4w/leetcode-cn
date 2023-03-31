#
# @lc app=leetcode.cn id=448 lang=python
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for num in nums:
            x = (num-1) % n
            nums[x] += n
        ans = [i+1 for i in range(n) if nums[i] <= n]
        return ans
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    nums = [4,3,2,7,8,2,3,1]
    ans = solution.findDisappearedNumbers(nums)
    print(ans)

