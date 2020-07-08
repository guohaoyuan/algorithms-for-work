"""
堆排序原理：
    利用大顶堆或者小顶堆进行排序。一般是二叉堆
    具有两个性质：
        1. 父节点值大于等于子节点的值
        2. 每个节点的左子树和右子树都是一个二叉堆

其逻辑结构是树，存储结构是层序遍历
    i节点的父节点下标就是(i-1)/2.
    他的左右子节点下标分别为2*i + 1 和 2*i+2

如何插入一个元素？
    新元素被加到存储结构的最后，其父节点到根节点是一个有序数组，现在的任务就是将这个新数据插入到有序数组中

如何删除一个元素？
    删除操作发生在根节点处，用最后一个元素填补空缺位置，然后恢复堆条件

堆排序：
    明显叶子节点都是已经是堆了，而叶子节点的数目占据一半，所以开始位置n//2-1,结束位置0
    对于每个位置执行下沉操作

"""