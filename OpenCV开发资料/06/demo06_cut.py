import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread("lena.png")  # 使用imread函数读取名为lena.png的图片
cv2.imshow('img', img[200:400, 300:500])
cv2.waitKey(0)  # 等待按键的按下
