import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('three.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 通过cv2.imshow()函数展示原图
dst = cv2.erode(img, (3, 3), iterations=5)  # 通过cv2.erode()函数进行膨胀，设置膨胀次数为5
cv2.imshow('膨胀', dst)  # 通过cv2.imshow()函数展示膨胀之后的图像
cv2.waitKey(0)  # 等待下一次按键按下
