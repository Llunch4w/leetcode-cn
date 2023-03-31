#
# @lc app=leetcode.cn id=406 lang=python
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 高个子会影响矮个子，同样身高的大k会影响小k
        n = len(people)
        ans = [[] for _ in range(n)]
        people.sort(key=lambda person: (person[0], -person[1]))
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans
            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    res = solution.reconstructQueue(people)
    print(res)