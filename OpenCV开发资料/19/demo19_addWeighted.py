import cv2  # opencv的缩写为cv2，导入opencv

img1 = cv2.imread('cat.bmp', 1)  # flags参数为1，返回彩色图像
img2 = cv2.imread('dog.bmp', 1)  # flags参数为1，返回彩色图像
imgAddW1 = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)  # 使用cv2.addWeighted函数进行图像融合，图片1和图片2权重比为0.3：0.7
cv2.imshow('图像1', imgAddW1)  # 通过cv2.imshow()函数展示融合的图像1
imgAddW2 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)  # 使用cv2.addWeighted函数进行图像融合，图片1和图片2权重比为0.5：0.5
cv2.imshow('图像2', imgAddW2)  # 通过cv2.imshow()函数展示融合的图像2
imgAddW3 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)  # 使用cv2.addWeighted函数进行图像融合，图片1和图片2权重比为0.7：0.3
cv2.imshow('图像3', imgAddW3)  # 通过cv2.imshow()函数展示融合的图像3
cv2.waitKey(0)  # 等待下一次按键按下
