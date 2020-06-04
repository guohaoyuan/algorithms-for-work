# -*- coding : utf-8 -*-
"""
计算iou(bbox1 bbox2)
1. 获取两个bbox的左上角右下角坐标
2. 获取相交矩形的左上角和右下角坐标
3. 计算相交矩形的面积 inter_area
4. 计算两个bbox1 bbox2的面积
5. inter_area / (b1_area + b2_area - inter_area)
"""

import torch

def bbox_iou(bbox1, bbox2):
    """
    计算两个bbox1 bbox2之间的iou，根据图形更方便理解
    :param bbox1: shape [n, 4]
    :param bbox2: shape [n, 4]
    :return: 返回iou
    """
    # 1. 获取两个bbox的左上角和右下角
    bbox1_x1, bbox1_y1, bbox1_x2, bbox1_y2 = bbox1[:, 0], bbox1[:, 1], bbox1[:, 2], bbox1[:, 3]
    bbox2_x1, bbox2_y1, bbox2_x2, bbox2_y2 = bbox2[:, 0], bbox2[:, 1], bbox2[:, 2], bbox2[:, 3]

    # 2. 计算相交矩形的左上角和右下角
    inter_x1 = torch.max(bbox1_x1, bbox2_x1)
    inter_y1 = torch.max(bbox1_y1, bbox2_y1)
    inter_x2 = torch.min(bbox1_x2, bbox2_x2)
    inter_y2 = torch.min(bbox1_y2, bbox2_y2)

    # 3. 计算相交矩形的面积
    inter_area = torch.clamp(inter_x2 - inter_x1 + 1, min=0) * torch.clamp(inter_y2 - inter_y1, min=0)

    # 4. 计算bbox1 bbox2的面积
    bbox1_area = (bbox1_x2 - bbox1_x1 + 1) * (bbox1_y2 - bbox1_y1 + 1)
    bbox2_area = (bbox2_x2 - bbox2_x1 + 1) * (bbox2_y2 - bbox2_y1 + 1)


    # 5. 计算iou
    iou = inter_area / (bbox1_area + bbox2_area - inter_area)
    return iou

