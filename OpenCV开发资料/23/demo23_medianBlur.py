import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lena.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 通过cv2.imshow()函数展示原图
dst = cv2.medianBlur(img, 3)  # 核大小设置为3,通过cv2.medianBlur()函数进行中值滤波
cv2.imshow('中值滤波', dst)  # 通过cv2.imshow()函数展示中值滤波之后的图像
cv2.waitKey(0)  # 等待下一次按键按下
