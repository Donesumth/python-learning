import cv2  # opencv的缩写为cv2，导入opencv
import numpy as np  # 导入numpy库

img = np.zeros((512, 512, 3), np.uint8)  # 创建一副512x512的黑色图片
cv2.imshow('img', img)  # 使用imshow函数展示创建的黑色图片
cv2.rectangle(img, (0, 0), (512, 512), (255, 0, 0), 5)  # 画一个起点为（0，0），画线终点为（512，512），线条颜色为蓝色。线条宽度为5的矩形
cv2.imshow('rectangle', img)  # 使用imshow函数展示画线之后的图像
cv2.waitKey(0)  # 等待按键的按下
