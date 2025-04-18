import cv2  # opencv的缩写为cv2，导入opencv
import numpy as np  # 导入numpy库

img = np.zeros((512, 512, 3), np.uint8)  # 创建一副512x512的黑色图片
cv2.imshow('img', img)  # 使用imshow函数展示创建的黑色图片
# 'www.baidu.com'为要显示的文字
# (10, 256)为文字开始的坐标
# cv2.FONT_HERSHEY_SIMPLEX为字体类型
# 字体大小设置为1
# 三个颜色通道设置为(255, 255, 255)，表示白色
# 线条粗细大小设置为2
cv2.putText(img, 'www.baidu.com', (10, 256), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow('text', img)  # 使用imshow函数展示文字
cv2.waitKey(0)  # 等待按键的按下
