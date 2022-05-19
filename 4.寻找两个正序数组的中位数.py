#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, len(nums1)
        nums1Mid, nums2Mid = 0, 0
        k = (len(nums1) + len(nums2) + 1) // 2
        while low <= high:
            nums1Mid = (low + high) // 2
            nums2Mid = k - nums1Mid
            if nums1Mid != len(nums1) and nums1[nums1Mid] < nums2[nums2Mid - 1]:
                low += 1
            elif nums1Mid > 0 and nums2[nums2Mid] < nums1[nums1Mid - 1]:
                high -= 1
            else:
                break
        is_odd = (len(nums1) + len(nums2)) % 2
        midLeft, midRight = 0, 0
        if nums1Mid == 0:
            midLeft = nums2[nums2Mid-1]
        else:
            midLeft = max(nums1[nums1Mid-1], nums2[nums2Mid-1])
        if is_odd:
            return round(midLeft, 5)
        if nums1Mid == len(nums1):
            midRight = nums2[nums2Mid]
        else:
            midRight = min(nums1[nums1Mid], nums2[nums2Mid])
        
        res = (midLeft + midRight) / 2
        return round(res, 5)
        
        
# @lc code=end

