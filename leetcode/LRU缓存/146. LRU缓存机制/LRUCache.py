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
        if self.size == 0:  #### 易错
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
            self.cache.remove(self.map[key])
            self.cache.addFirst(new_item)
            self.map[key] = new_item            #### 易错
        else:
            if self.capacity == self.cache.getSize():
                last_node = self.cache.removeLast()
                self.map.pop(last_node.key)     #### 易错
            self.cache.addFirst(new_item)
            self.map[key] = new_item            #### 易错