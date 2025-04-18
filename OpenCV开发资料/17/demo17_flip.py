import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lena.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 使用cv2.imshow()函数进行原图展示
dst1 = cv2.flip(img, 0)  # 使用cv2.flip函数对img图像进行水平翻转
cv2.imshow('水平翻转', dst1)  # 使用cv2.imshow()函数进行缩放图像的展示
dst2 = cv2.flip(img, 1)  # 使用cv2.flip函数对img图像进行垂直翻转
cv2.imshow('垂直翻转', dst2)  # 使用cv2.imshow()函数进行缩放图像的展示
dst3 = cv2.flip(img, -1)  # 使用cv2.flip函数对img图像进行水平垂直翻转
cv2.imshow('水平垂直翻转', dst3)  # 使用cv2.imshow()函数进行缩放图像的展示
cv2.waitKey(0)  # 等待下一次按键按下
