import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lena.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 使用cv2.imshow()函数进行原图展示
dst1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # 使用cv2.rotate函数对img图像进行顺时针旋转90
cv2.imshow('顺时针旋转90', dst1)  # 使用cv2.imshow()函数进行旋转之后的图像进行展示
dst2 = cv2.rotate(img, cv2.ROTATE_180)  # 使用cv2.rotate函数对img图像进行水平旋转
cv2.imshow('水平旋转', dst2)  # 使用cv2.imshow()函数进行旋转之后的图像进行展示
dst3 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 使用cv2.rotate函数对img图像进行逆时针旋转90
cv2.imshow('逆时针旋转90', dst3)  # 使用cv2.imshow()函数进行旋转之后的图像进行展示
cv2.waitKey(0)  # 等待下一次按键按下
