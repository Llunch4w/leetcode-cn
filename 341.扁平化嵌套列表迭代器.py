#
# @lc app=leetcode.cn id=341 lang=python
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, item):
        self.list = []
        self.integer = None
        if type(item) == list:
            self.list = item
        else:
            self.integer = item

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        if self.integer:
            return True

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.integer

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.list


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for i in range(len(nestedList)-1, -1, -1):
            if nestedList[i].getList() and len(nestedList[i].getList()) == 0:
                continue
            self.stack.append(nestedList[i])       

    def next(self):
        """
        :rtype: int
        """
        item = self.stack.pop()
        if item.isInteger():
            return item.getInteger()
        else:
            while item.getInteger() == None:
                item_list = item.getList()
                for i in range(len(item_list)-1, -1, -1):
                    self.stack.append(item_list[i])
                item = self.stack[-1]
            item = self.stack.pop()
            return item.getInteger()    

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

if __name__ == "__main__":
    nested_list = [NestedInteger([])]
    iterator = NestedIterator(nested_list)
    while iterator.hasNext():
        print(iterator.next())