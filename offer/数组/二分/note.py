"""
关于二分法个人心得：
1. 二分法：一般是while L <= R:         （对于此处是否加=应该这样理解：加=结果是R越过L；不加=是R相遇L，由于结果返回依赖L，故没产生不利影响
且在其下面一开始更新mid = (L + R) // 2

2. 返回的都与LR两指针相遇时有关
"""