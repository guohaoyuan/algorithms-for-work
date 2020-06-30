'直方图均衡化函数，0::28 2019/06/20'

__author__ = 'ghy'

import numpy as np
import cv2 as cv


# 创建空列表(数组)
def createEmptyList(size):
    newList = []
    for eachNum in range(0, size):
        newList.append(0)
    return newList


# 创建空图像矩阵
def createEmptyImage(rows, cols, type):
    img = np.zeros((rows, cols), dtype=type)
    return img


# 直方图均衡化
def histequaLize(src, dst):
    # step 1 校验参数#
    assert (type(src) == np.ndarray)
    assert (src.dtype == np.uint8)
    assert (type(dst) == np.ndarray)
    assert (dst.dtype == np.uint8)

    # step 2 直方图统计#
    hist = createEmptyList(256)
    rows, cols = src.shape
    for r in range(rows):
        for c in range(cols):
            hist[src[r, c]] += 1

    # step 3 直方图归一化#
    for each in range(256):
        hist[each] /= rows * cols

    # step 4 直方图累加#
    for each in range(1, 256):
        hist[each] = hist[each - 1] + hist[each]

    # step 4 均衡#
    for each in range(256):
        hist[each] = (np.uint8)(255 * hist[each] + 0.5)

    for r in range(rows):
        for c in range(cols):
            dst[r, c] = hist[src[r, c]]


def histMain():
    img = cv.imread('2.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    dst = createEmptyImage(img.shape[0], img.shape[1], np.uint8)
    histequaLize(gray, dst)
    cv.imshow('histEnhance.jpg', dst)
    cv.waitKey(0)


if __name__ == '__main__':
    histMain()
