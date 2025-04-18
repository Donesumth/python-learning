import cv2  # opencv的缩写为cv2，导入opencv

img1 = cv2.imread('lena.png', 0)  # flags参数为0，返回灰色图像
img2 = cv2.imread('lena.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('灰度图', img1)  # imshow函数现实处理结果
cv2.imshow('彩色图', img2)
cv2.waitKey(0)  # 等待下一次按键按下
