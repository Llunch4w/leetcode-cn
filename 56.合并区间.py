#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 按照左端点排序
        sorted_intervals = sorted(intervals, key=lambda item: item[0])
        # merge_list
        merge_list = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            last_interval = merge_list[-1]
            cur_interval = sorted_intervals[i]
            # 如果当前区间大左端点 < 上个区间的右端点，则合并
            if cur_interval[0] <= last_interval[1]:
                new_interval = [last_interval[0], max(cur_interval[1], last_interval[1])]
                merge_list[-1] = new_interval
            else:
                merge_list.append(cur_interval)
        return merge_list
                
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    res = solution.merge(intervals)
    print(res)

