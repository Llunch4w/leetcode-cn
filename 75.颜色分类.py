#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0
        for i, num in enumerate(nums):
            if num == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
            elif num == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                # 如果 p0 < p1, 则交换时可能将已排序好的 1 交换出去，需要再交换回来
                if p0 < p1:
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1
        return nums
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    nums = [2,0,2,1,1,0]
    res = solution.sortColors(nums)
    print(res)

