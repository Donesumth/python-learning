import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lena.png', 0)  # flags参数为0，返回灰色图像
cv2.imshow('灰度图', img)  # imshow函数现实处理结果
cv2.imwrite('lena_gray.png', img)  # imwrite写入读取到的图像并命名为lena_gray.png
cv2.waitKey(0)  # 等待下一次按键按下
