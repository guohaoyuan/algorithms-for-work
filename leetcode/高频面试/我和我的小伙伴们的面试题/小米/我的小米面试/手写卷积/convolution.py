import numpy as np

def convolution(k, data):
    """
    实现简单的卷积操作
    :param k: numpy数组
    :param data: numpy数组
    :return: 返回卷积后的操作
    """
    n, m = data.shape   # 输入图片的深度和宽度
    img_new = []        # 存储输出结果
    for i in range(n-3):# 假设卷积核是3*3
        line = []       # 存放每一行滑窗的结果
        for j in range(m-3):
            a = data[i:i+3, j:j+3]   # 将要卷积的窗口
            line.append(np.sum(np.multiply(k, a)))  # 进行卷积，逐元素相乘，在相加，存储进line
        img_new.append(line)
    return np.array(img_new)

if __name__ == '__main__':
    k = np.array([
        [0, 1, 2],
        [2, 2, 0],
        [0, 1, 2]
    ])
    data = np.array([
        [52, 58, 55, 139, 133, 91],
       [46, 53, 52, 140, 138, 103],
       [45, 53, 52, 142, 144, 119],
       [40, 37, 37, 60,  61, 47],
       [39, 36, 37, 56, 58, 48],
       [35, 33, 35, 54, 57, 48]
    ])
    res = convolution(k, data)
    print(res)