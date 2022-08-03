#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
# Min Heap
class MinHeap(object):
    def __init__(self):
        self.data = []
        self.data_size = 0
        
    def insert(self, num):
        self.data.append(num)
        self.data_size += 1
        index = self.data_size - 1
        while index > 0:
            parent = (index - 1)//2
            if self.data[parent] > self.data[index]:
                self.data[parent], self.data[index] = self.data[index], self.data[parent]
                index = parent
            else:
                break
    
    def adjust(self):
        if len(self.data) == 0:
            return     
        index = 0
        while index * 2 + 1 < self.data_size:
            left_index = index * 2 + 1
            right_index = -1
            if index * 2 + 2 < self.data_size:
                right_index = index * 2 + 2
            if right_index != -1 and self.data[right_index] < self.data[left_index]:
                if self.data[index] < self.data[right_index]:
                    break
                self.data[index], self.data[right_index] = self.data[right_index], self.data[index]
                index = right_index
            else:
                if self.data[index] < self.data[left_index]:
                    break
                self.data[index], self.data[left_index] = self.data[left_index], self.data[index]
                index = left_index 
                
    def replace_root(self, num):
        self.data[0] = num    
        
    def get_root(self):
        return self.data[0]       
                    
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = MinHeap()
        for i in range(k):
            min_heap.insert(nums[i])
        for i in range(k, len(nums)):
            min_num = min_heap.get_root()
            if nums[i] > min_num:
                min_heap.replace_root(nums[i])
                min_heap.adjust()
        return min_heap.get_root()
        
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [3,2,1,5,6,4]
#     k = 2
#     print(solution.findKthLargest(nums, k))
# @lc code=end

