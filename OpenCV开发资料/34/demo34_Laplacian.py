import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('number.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 通过cv2.imshow()函数展示原图
laplacian = cv2.Laplacian(img, cv2.CV_64F)  # 使用Laplacian算子进行边缘检测，数据类型设置为cv2.CV_64F
laplacian = cv2.convertScaleAbs(laplacian)  # 计算绝对值
cv2.imshow('laplacian', laplacian)  # 通过cv2.imshow()函数展示Laplacian算子边缘检测计算之后的图像
cv2.waitKey(0)  # 等待下一次按键按下
