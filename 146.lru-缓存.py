#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存
#
        
# HashMap + Bidirection_List
# @lc code=start
class DLinkNode(object):
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next
        
    def __str__(self):
        return "key={};value={}".format(self.key, self.value)
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        head_soldier, tail_soldier = DLinkNode(0, -1), DLinkNode(0, -1)
        head_soldier.next = tail_soldier
        tail_soldier.pre = head_soldier
        self.head_soldier = head_soldier
        self.tail_soldier = tail_soldier
        self.remain_capacity = capacity
        self.hash_map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_map:
            return -1
        self._move2head(self.hash_map[key])
        return self.hash_map[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.remain_capacity == 0 and key not in self.hash_map:
            node_key = self._remove_last()
            del self.hash_map[node_key]
            
        if key in self.hash_map:
            old_node = self.hash_map[key]
            old_node.value = value
            self._move2head(old_node)
        else:
            new_node = DLinkNode(key, value)
            # print(new_node)
            self.hash_map[key] = new_node
            self.remain_capacity -= 1
            head_next = self.head_soldier.next
            new_node.pre = self.head_soldier
            new_node.next = head_next
            head_next.pre = new_node
            self.head_soldier.next = new_node
            # print(new_node)
                    
    def _move2head(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = self.head_soldier
        self.head_soldier.next.pre = node
        node.next = self.head_soldier.next
        self.head_soldier.next = node
        
    def _remove_last(self):
        last_node = self.tail_soldier.pre
        # print(last_node.value)
        last_node.pre.next = self.tail_soldier
        self.tail_soldier.pre = last_node.pre
        last_node.pre = None
        last_node.next = None
        self.remain_capacity += 1
        return last_node.key

# if __name__ == "__main__":
#     a = LRUCache(2)
#     a.put(1, 1)
#     a.put(2, 2)
#     print(a.get(1))
#     a.put(3, 3)
#     print(a.get(2))
#     a.put(4, 4)
#     print(a.get(1))
#     print(a.get(3))
#     print(a.get(4))
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

