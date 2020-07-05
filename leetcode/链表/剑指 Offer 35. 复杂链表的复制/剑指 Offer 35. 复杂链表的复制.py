"""
1. 复制克隆节点，接在母节点的后面，使用curM, curC两个 指针就够了
2. 将母节点的随机指针复制给克隆节点，有一点是，要注意母节点随机指针是否存在
3. 还原链表，有一点是，需要用到.next.next, 所以就要使用nextM指针
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def cloneNode(node):
            curM = node

            while True:
                if not curM:
                    return
                    # 将当前克隆节点加入母节点后面
                curC = Node(curM.val)
                curC.next = curM.next
                curM.next = curC

                # 母节点指针后移
                curM = curC.next

        def randomNode(node):
            curM = node

            while curM:
                curC = curM.next

                # 当前母节点的random存在
                if curM.random:
                    curC.random = curM.random.next
                # 否则就是指向空
                # 更新母节点
                curM = curC.next
            return

        def recovery(node):
            curM = node
            curC = curM.next
            nextM = curC.next
            # res记录返回结果
            res = curC

            while nextM:
                # 连接克隆节点
                curC.next = nextM.next
                # 回复原节点
                curM.next = nextM

                # 更新节点
                curC = curC.next
                curM = nextM
                nextM = curC.next
            return res

        if not head:
            return head

        cloneNode(head)
        randomNode(head)

        return recovery(head)