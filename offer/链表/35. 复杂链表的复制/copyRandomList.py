# -*- coding : utf-8 -*-



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head):
        """

        :param head:
        :return: 返回复制链表
        """
        # 1. 克隆节点连接到原链表中
        def clone_list(head):
            # 1.1 初始化当前母节点
            curM = head

            # 1.2 当前母节点存在情况
            while curM:
                # 1.2.1 初始化下一母节点
                nextM = curM.next
                # 初始化当前克隆节点
                curC = Node(curM.val)
                # 将当前克隆节点添加到链表中
                curM.next = curC
                curC.next = nextM
                # 更新当前母节点
                curM = nextM

        # 2. 创建克隆节点的random指针
        def random_list(head):
            # 2.1 初始化当前母节点
            curM = head

            # 2.2 当前母节点存在
            while curM:
                # 初始化下一母节点
                nextM = curM.next.next

                # 初始化当前克隆节点
                curC = curM.next

                # 如果当前母节点random指针存在情况下
                if curM.random:
                    # 当前克隆节点的random指针，指向当前母节点random一个节点
                    curC.random = curM.random.next

                # 更新当前母节点
                curM = nextM

        # 3. 将链表断开
        def reconnect_list(head):
            # 3.1 初始化当前母节点，和返回结果
            curM = head
            res = None

            # 3.2 如果当前母节点存在，为了应对链表只有一个节点的情况

            # 初始化下一母节点
            nextM = curM.next.next

            # 初始化当前克隆节点
            curC = curM.next
            res = curC

            # 3.3 如果下一母节点存在，为了应对长度大于1的链表
            while nextM:
                # 当前克隆节点连接
                curC.next = nextM.next
                # 当前母节点连接，没多大意义，完全为了还原输入
                curM.next = nextM
                # 更新当前克隆节点和下一个母节点
                curC = curC.next
                nextM = curC.next
            return res
        #
        if not head:
            return head
        clone_list(head)
        random_list(head)
        return reconnect_list(head)