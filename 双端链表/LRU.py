# Pingcap后端研发一面惨挂

# 每个node都是一个键值对+双向链表
class Node:
    __slots_ = 'prev', 'next', 'key', 'value'
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = dict()
    
    
    def get_node(self, key):
        # 如果不在字典中，直接返回None
        if key not in self.key_to_node:
            return None
        # 如果在字典中，则提取他，并把它提到最前
        node = self.key_to_node[key]
        self.remove(node)
        self.push_front(node)
        return node
    
    def get(self,key):
        node = self.get_node(key)
        return node.value if node else -1
    
    def put(self, key, value):
        # 先看是否在字典中，如果在，则说明是更新
        node = self.get_node(key)
        if node:
            node.value = value
            return
        # 更新并提取值
        self.key_to_node[key] = node = Node(key, value)
        self.push_front(node)
        # 不然的话，就相当于插入，插入需要检测是否长度大于容量，如果大于，就删除末尾
        if len(self.key_to_node) > self.capacity:
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)
    
    
    def remove(self, x):
        # 使他前节点的后节点成为他的后节点，使他后节点的前节点成为他的前节点
        x.prev.next = x.next
        x.next.prev = x.prev

    def push_front(self,x):
        # 使他前节点成为哨兵，他的后节点成为原来的头节点，同时使他前节点的后节点成为他的后节点，使他后节点的前节点成为他的前节点
        x.prev = self.dummy
        x.next = self.dummy.next
        # 使哨兵的前节点成为他，使原先头节点的前节点成为他
        x.prev.next = x
        x.next.prev = x