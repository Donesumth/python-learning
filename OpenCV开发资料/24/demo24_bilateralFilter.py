import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lena.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 通过cv2.imshow()函数展示原图
dst = cv2.bilateralFilter(img, 9, 150, 150)  # 空间距离参数设置为9，sigmaColor和sigmaSpace值设置为150,通过cv2.bilateralFilter()函数进行双边滤波
cv2.imshow('双边滤波', dst)  # 通过cv2.imshow()函数展示双边滤波之后的图像
cv2.waitKey(0)  # 等待下一次按键按下
