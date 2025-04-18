import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lean.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 通过cv2.imshow()函数展示原图
dst = cv2.GaussianBlur(img, (0, 0), 10)  # 卷积核为(0,0),通过cv2.GaussianBlur()函数进行高斯滤波
cv2.imshow('高斯滤波', dst)  # 通过cv2.imshow()函数展示高斯滤波之后的图像
cv2.waitKey(0)  # 等待下一次按键按下
