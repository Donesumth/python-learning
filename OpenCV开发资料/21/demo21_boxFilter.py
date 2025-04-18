import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lean.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 通过cv2.imshow()函数展示原图
dst1 = cv2.blur(img, (3, 3))  # 卷积核为(3,3),通过cv2.blur()函数进行均值滤波函
cv2.imshow('均值滤波', dst1)  # 通过cv2.imshow()函数展示均值滤波之后的图像
dst2 = cv2.boxFilter(img, -1, (3, 3))  # 卷积核为(3,3),通过cv2.boxFilter()函数进行方框滤波函
cv2.imshow('方框滤波', dst2)  # 通过cv2.imshow()函数展示方框滤波之后的图像
dst3 = cv2.boxFilter(img, -1, (3, 3), normalize=0)  # 卷积核为(3,3),通过cv2.boxFilter()函数进行方框滤波函
cv2.imshow('非归一化方框滤波', dst3)  # 通过cv2.imshow()函数展示方框滤波之后的图像
cv2.waitKey(0)  # 等待下一次按键按下
