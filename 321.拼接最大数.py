#
# @lc app=leetcode.cn id=321 lang=python
#
# [321] 拼接最大数
#

# @lc code=start
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_nums = []
        for i in range(k+1):
            if len(nums1) < i or len(nums2) < k-i:
                continue
            nums_a = self.getMax(nums1, i)
            nums_b = self.getMax(nums2, k-i)
            max_nums = max(max_nums, self.merge(nums_a, nums_b))
        return max_nums
    
    def getMax(self, nums, k):
        drop = len(nums) - k
        stack = []
        for num in nums:
            while drop and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:k]
    
    def merge(self, nums1, nums2):
        nums = []
        while nums1 or nums2:
            bigger = nums1 if nums1 > nums2 else nums2
            nums.append(bigger.pop(0))
        return nums
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    nums1 = [6,7]
    nums2 = [6,0,4]
    k = 5
    print(solution.maxNumber(nums1, nums2, k))