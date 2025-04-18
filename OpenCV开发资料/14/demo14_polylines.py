import cv2  # opencv的缩写为cv2，导入opencv
import numpy as np  # 导入numpy库

img = np.zeros((512, 512, 3), np.uint8)  # 创建一副512x512的黑色图片
cv2.imshow('img', img)  # 使用imshow函数展示创建的黑色图片
pts = np.array([[50, 0], [100, 500], [400, 400], [500, 0]])  # 四个坐标值，代表多边形的四个角
cv2.polylines(img, [pts], True, (0, 255, 255), 5)  # 使用cv2.polylines函数将四个点进行连接，True指代图形闭合，线宽为5
cv2.imshow('polylines', img)  # 使用imshow函数展示多边形图像
cv2.waitKey(0)  # 等待按键的按下
