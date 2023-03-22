#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 从后往前找第一对升序对
        k = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break
        if k == -1:
            nums[:] = nums[::-1]
            return
        # 找一个最接近的 j 和 i 进行交换
        j = len(nums)-1
        # 从后往前找第一个大于 nums[k] 的 nums[j]
        while j > k+1 and nums[j] <= nums[k]:
            j -= 1
        # 交换 nums[k+1] 和 nums[j] 的位置
        nums[k], nums[j] = nums[j], nums[k]
        # 让 [k+1, end) 升序
        nums[k+1:] = nums[k+1:][::-1]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,1]
    print(nums)
    solution.nextPermutation(nums)
    print(nums)
