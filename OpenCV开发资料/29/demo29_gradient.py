import cv2  # opencv的缩写为cv2，导入opencv
import numpy as np  # numpy数值计算工具包

img = cv2.imread('circle.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 通过cv2.imshow()函数展示原图
kernel = np.ones((5, 5), np.uint8)  # 创建5x5的卷积核
dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  # 通过cv2.morphologyEx函数进行形态学运算，op设置为cv2.MORPH_GRADIENT表示为梯度运算
cv2.imshow('梯度运算', dst)  # 通过cv2.imshow()函数展示梯度运算之后的图像
cv2.waitKey(0)  # 等待下一次按键按下
