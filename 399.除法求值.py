#
# @lc app=leetcode.cn id=399 lang=python
#
# [399] 除法求值
#

# @lc code=start
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        class UnionSet(object):
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                # weight 保存子节点/父节点的值
                self.weight = [1.0 for _ in range(n)]
                
            def find(self, node):
                '''路径压缩'''
                if self.parent[node] == node:
                    return node
                origin_parent = self.parent[node]
                self.parent[node] = self.find(origin_parent)
                self.weight[node] *= self.weight[origin_parent]
                return self.parent[node]
            
            def union(self, x, y, val):
                '''归并'''
                x_root = self.find(x)
                y_root = self.find(y)
                if x_root == y_root:
                    return
                self.parent[x_root] = y_root
                self.weight[x_root] = self.weight[y] * val / self.weight[x]
                
            def compare(self, x, y):
                if x is None or y is None:
                    return -1.0
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    return -1.0
                return self.weight[x] / self.weight[y]
                
        union_set = UnionSet(2 * len(equations))
        letter2id = {}
        index = 0
        for equation, value in zip(equations, values):
            x, y = equation
            if x not in letter2id:
                letter2id[x] = index
                index += 1
            if y not in letter2id:
                letter2id[y] = index
                index += 1
            union_set.union(letter2id[x], letter2id[y], value)
        
        answers = []
        for query in queries:
            x, y = query
            if x not in letter2id or y not in letter2id:
                answers.append(-1.0)
                continue
            res = union_set.compare(letter2id[x], letter2id[y])
            answers.append(res)
        return answers
            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    equations = [["a","b"]]
    values = [0.5]
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    answers = solution.calcEquation(equations, values, queries)
    print(answers)
