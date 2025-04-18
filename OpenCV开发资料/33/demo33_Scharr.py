import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('number.png', 1)  # flags参数为1，返回彩色图像
cv2.imshow('原图', img)  # 通过cv2.imshow()函数展示原图
scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)  # 使用Sobel算子进行边缘检测，数据类型设置为cv2.CV_64F,只算x方向梯度,Sobel核大小设置为3
scharrx = cv2.convertScaleAbs(scharrx)  # 计算绝对值
cv2.imshow('scharrx', scharrx)  # 通过cv2.imshow()函数展示x方向梯度边缘检测计算之后的图像
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)  # 使用Sobel算子进行边缘检测，数据类型设置为cv2.CV_64F,只算x方向梯度,Sobel核大小设置为3
scharry = cv2.convertScaleAbs(scharry)  # 计算绝对值
cv2.imshow('scharry', scharry)  # 通过cv2.imshow()函数展示y方向梯度边缘检测计算之后的图像
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)  # 图像融合的系数比为0.5：0.5，0表示偏置项
cv2.imshow('sobelxy', scharrxy)  # 通过cv2.imshow()函数展示融合之后的图像
cv2.waitKey(0)  # 等待下一次按键按下
