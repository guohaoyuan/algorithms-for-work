"""
59-1 59-2 30相似度很高
其中由于30是栈操作，所以维护最大栈时候，用if判断是否进入辅助栈
其中由于59-2是双端队列，所以维护时候用while判断是否弹出，然后添加到辅助双端队列
整体来说，都是维护了一个单调递减辅助
"""