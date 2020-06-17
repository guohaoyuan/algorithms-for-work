# -*- coding : utf-8 -*-
# 可参考：https://blog.csdn.net/u012052268/article/details/105989026
"""
nms是一种祛除冗余框的过程
步骤如下：
for cls in all cls:
    1. 获取当前cls对应的左上角，右下角，scores信息，并计算面积
    2. 降序排列scores，并记录当前最大score的框
    3. 当前score最大的框与剩余的框计算iou，并去除大于阈值的框
    4. 对于剩余的框，循环执行2. 3. 直到所有的框均满足要求，即不能在去除框
"""

import numpy as np


def nms(predicts_dict, threshold=0.5):
    """

    :param predicts_dict: {"stick": [[x1 y1 x2 y2 score], [...]]}
    :param threshold: iou threshold
    :return:
    """
    # 首先对于每一个类别的目标分别进行nms
    for object_name, bbox in predicts_dict.items(): # items() 函数以列表返回可遍历的(键, 值) 元组数组
        # 将tensor转换为np数组
        bbox_array = np.array(bbox, dtype=np.float)
        # shape [n, 5]

        # 1. 获取当前类的所有矩形框坐标和scores，并计算bbox的面积
        x1, y1, x2, y2, scores = bbox_array[:, 0], bbox_array[:, 1], bbox_array[:, 2], bbox_array[:, 3], bbox_array[:, 4]
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)


        # 2.1 按照scores降序排列
        order = scores.argsort()[::-1]

        keep = []   # 用于保存最终保留下来的bbox对应的索引

        # 一次按照scores从高到低遍历bbox，去除大于阈值的bbox

        while order.size > 0:
            i = order[0]    # 2.2 记录当前score最大的bbox对应索引

            keep.append(i)  # 添加到keep，表示保留下来

            # 3.1 计算iou
            # 计算当前score最大的框和其余框的相交矩形坐标
            inter_x1 = np.maximum(x1[i], x1[order[1:]])
            inter_y1 = np.maximum(y1[i], y1[order[1:]])
            inter_x2 = np.minimum(x2[i], x2[order[1:]])
            inter_y2 = np.minimum(y2[i], y2[order[1:]])

            # 计算相交矩形的面积
            inter_area = np.maximum(0.0, inter_x2 - inter_x1 + 1) * np.maximum(0.0, inter_y2 - inter_y1 + 1)
            iou = inter_area / (areas[i] + areas[order[1:]] - inter_area)
            # 3.2 去除大于阈值的框
            # 首先找到小于阈值的索引，之所以+1,是因为没有计算自身的iou
            indexs = np.where(iou < threshold)[0] + 1
            # 4. 保留剩余框，继续迭代
            order = order[indexs]

            print("iou = {}, keep = {}, indexs = {}, order = {}".format(iou, keep, indexs, order))
        bbox = bbox_array[keep]
        # 修改对应类的框
        predicts_dict[object_name] = bbox.tolist()
        predicts_dict = predicts_dict
    return predicts_dict

if __name__ == '__main__':
    predict_dict = {'cup': [[59, 120, 137, 368, 0.124648176], [221, 89, 369, 367, 0.35818103], [54, 154, 148, 382, 0.13638769]]}
    print(nms(predict_dict))