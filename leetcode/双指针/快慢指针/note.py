"""
快慢指针的模板

if not head:
    return None或者head       # 特殊情况


slow, fast = head, head     # 初始化快慢指针

while True:                 # 在循环里就可以按照常规逻辑从前向狗判断
    if not fast or not fast.next:   # fast指针走两步,所以不能让fast走到头还要走
        return None或者其他
    else:
        fast = fast.next.next
        slow = slow.next

    # 根据需要是否添加其他判断


"""