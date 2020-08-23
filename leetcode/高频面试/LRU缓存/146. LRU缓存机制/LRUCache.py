"""
分析:

要求插入和删除的时间复杂度均为o(1)

思考:
哈希表的查找时间复杂度为1, 但是无序结构
链表的删除插入时间复杂度为1, 有序结构, 查找慢

创建class类node 创建双端链表

创建DoubleList 实现双端链表的如下操作:
                                    remove删除指定节点: 调用了已有节点需要删除后,再插入头部
                                    removeLast删除最后一个节点: 因为当容量满了需要删除
                                    addFirst将指定节点插入头部: 因为删除操作后为了插入头部
                                    getSize需要一个函数获得当前双端链表不包括虚拟节点,的长度

在LRUCache类

    初始化哈希表和双端链表

    get函数,
        如果添加key不在哈希表中, 直接返回-1
        如果在哈希表中, 先利用哈希表查找当前key的value, 在利用put(key, value)方法把数据提前

    put函数
        先将key value转换成链表节点

        利用哈希表判断key对应的是否在哈希表中, 如果在哈希表中
                调用remove删除指定节点
                将删除节点提前addFirst
                在哈西表中添加映射
        如果不再哈希表中
                如果当前容量已经满了,
                                删除最后一个元素removeLast
                                在哈希表中中删除对应索引
                添加到头addFirst
                在哈希表中添加映射
"""


# 首先构建双向链表
class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class DoubleList:
    def __init__(self):
        # 设置哨兵
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFirst(self, x):
        # 在最前面添加节点x
        # 先将x前后连接上
        x.next = self.head.next
        x.prev = self.head
        # 从后往前修改
        self.head.next.prev = x
        self.head.next = x
        self.size += 1

    def remove(self, x):
        # 删除节点x, 要保证x一定存在
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeLast(self):
        # 删除链表的最后一个节点,并返回该节点；目的是能够在链表中删除元素,并在哈希表中删除对应元素
        if self.size == 0:  #### 可以删除
            return None

        last_node = self.tail.prev
        self.remove(last_node)
        return last_node

    def getSize(self):
        # 返回当前尺寸
        return self.size


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.cache = DoubleList()

    def get(self, key: int) -> int:
        """
        如果哈希表中不存在key,则直接返回
        否则, 利用哈希表查找数据,
        将其放在开头
        :param key:
        :return:
        """
        if key not in self.map:
            return -1

        val = self.map[key].val         #### 易错
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        """
        将要插入的key value创建链表节点
        如果key已经在哈希表中,
            先将其从链表中删除,
            然后添加到开头
            在哈希表中重新建立映射
        否则
            先判断是否超容量,超容量
                从链表中删除最后一个节点
                从哈希表中删除对应映射
            将新元素添加到开头
            并在哈希表中建立映射
        :param key:
        :param value:
        :return:
        """
        new_item = Node(key, value)
        if key in self.map:
            self.cache.remove(self.map[key])    # 必须通过查询哈希表的方式找到对应的节点
            self.cache.addFirst(new_item)
            self.map[key] = new_item            #### 易错
        else:
            if self.capacity == self.cache.getSize():
                last_node = self.cache.removeLast()
                self.map.pop(last_node.key)     #### 易错
            self.cache.addFirst(new_item)
            self.map[key] = new_item            #### 易错
        """
        易错点：
        1. 我们使用的节点是key val键值对，
        2. 哈希表中是key就是输入的key,value是node
        3. 在执行删除操作记得删除哈希表中的对应关系
        
        
        get(key, value)
        先创建节点node(key, val)
        如果节点不再其中，
            如果容量<=实际double size:    # 满了
                删除最后一个节点
                并删除哈希表中的对应关系
                添加node
                添加对应关系
            如果没满：
                直接添加
                并添加对应关系
        如果节点在其中
            无论是否满了，都要先删除对应节点，并删除对应的哈希表关系，然后在添加到double中，并添加哈希表的对应关系    
        """


class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None


class Double:
    def __init__(self):
        self.tail = Node(-1, -1)
        self.head = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def addFirst(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node
        self.size += 1

    def removeLast(self):
        # if self.size == 0:
        #     return -1
        last = self.tail.pre
        self.remove(last)
        return last

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1


class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.double = Double()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            val = self.hashmap[key].val
            self.put(key, val)
            return val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key not in self.hashmap:
            if self.capacity <= self.double.size:
                # 不在其中但超了
                last = self.double.removeLast()
                self.hashmap.pop(last.key)
                self.double.addFirst(node)
                self.hashmap[key] = node
            else:
                # 不在其中且未超
                self.hashmap[key] = node
                self.double.addFirst(node)
        else:
            # 在其中
            self.double.remove(self.hashmap[key])
            self.hashmap.pop(key)
            self.hashmap[key] = node
            self.double.addFirst(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None


class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def addFirst(self, node):
        tmp = self.head.next
        node.next = tmp
        node.pre = self.head
        self.head.next = node
        tmp.pre = node
        self.size += 1

    def removeLast(self):
        if self.size == 0:
            return None
        tmp = self.tail.pre
        tmp.pre.next = self.tail
        self.tail.pre = tmp.pre
        tmp.next = None
        tmp.pre = None
        self.size -= 1
        return tmp

    def remove(self, node):
        if self.size == 0:
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = None
        node.pre = None
        self.size -= 1


class LRUCache:

    def __init__(self, capacity: int):
        self.doubleList = DoubleList()
        self.hashmap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        tmp = self.hashmap[key]
        self.put(tmp.key, tmp.value)
        return tmp.value

    def put(self, key: int, value: int) -> None:
        # 创建节点
        node = Node(key, value)
        # 该节点不在哈希表中
        if key not in self.hashmap:
            # 此时没满
            if self.capacity > self.doubleList.size:
                # 加入到哈希表
                self.doubleList.addFirst(node)
                self.hashmap[key] = node

            else:
                # 满了
                tmp = self.doubleList.removeLast()
                # 删除对应关系
                self.hashmap.pop(tmp.key)
                # 加入哈希表
                self.doubleList.addFirst(node)
                self.hashmap[key] = node
        else:  # 该节点在哈希表中
            if self.capacity > self.doubleList.size:
                # 满了
                # 首先删除该节点
                tmp = self.hashmap[key]
                self.doubleList.remove(tmp)
                self.hashmap.pop(tmp.key)
                # 添加节点
                self.doubleList.addFirst(node)
                self.hashmap[key] = node
            else:
                # 没有满，直接添加
                # 首先删除
                tmp = self.hashmap[key]
                self.doubleList.remove(tmp)
                self.hashmap.pop(tmp.key)
                # 添加
                self.doubleList.addFirst(node)
                self.hashmap[key] = node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)