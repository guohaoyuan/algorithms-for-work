
"""
1. 首先得到左上角和右下角坐标, x1 y1 x2 y2;  计算面积
2. 对分数进行排序
3. 设置列表keep,保存去除冗余框的剩余框
4. 去除冗余框,
    需要计算最高score框与剩余框的iou
    根据阈值去除冗余框,将保留下来的框存入keep
    更新剩余框列表,进行重复操作
5. 剩余的框就是nms保留下来的
"""
import numpy as np


def nms(bboxes, scores, threshold=0.7):
    """

    :param bboxes: np [n, 4]
    :param scores: np (n, )
    :param threshold: float
    :return:
    """

    # 1. 首先获取左上点和右下点
    x1, y1, x2, y2 = bboxes[:, 0], bboxes[:, 1], bboxes[:, 2], bboxes[:, 3]

    # 计算面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    # 2. 对分数进行排序
    order = scores.argsort()[::-1]  #  默认升序, ::-1进行降序
    # print(order)
    # 3. 设置keep,保留
    keep = []

    # 4. 去除冗余框
    while order.size > 0:   # 经过不断的消除冗余,将其中剩余框化为0
        # 最高分数对应索引
        highest = order[0]
        keep.append(highest)
        # print(keep)
        # 计算iou
        # 计算最高分和剩余矩形相交矩形的面积
        inter_x1 = np.maximum(x1[highest], x1[order[1:]])
        inter_y1 = np.maximum(y1[highest], y1[order[1:]])
        inter_x2 = np.minimum(x2[highest], x2[order[1:]])
        inter_y2 = np.minimum(y2[highest], y2[order[1:]])

        inter_area = np.maximum(0.0, inter_x2 - inter_x1 + 1) * np.maximum(0.0, inter_y2 - inter_y1 + 1)

        iou = inter_area / (areas[highest] + areas[order[1:]] - inter_area)

        # 根据阈值将剩余框保留下来
        order = order[np.where(iou < threshold)[0] + 1]
        print("iou = {}, keep = {}, order = {}".format(iou, keep, order))

    bboxes = bboxes[keep]
    return bboxes

if __name__ == '__main__':
    bboxes = np.array([[59, 120, 137, 368], [221, 89, 369, 367], [54, 154, 148, 382]], dtype=float)
    scores = np.array([0.124648176, 0.35818103, 0.13638769], dtype=float)
    bboxes = nms(bboxes, scores, threshold=0.5)
    print(bboxes)