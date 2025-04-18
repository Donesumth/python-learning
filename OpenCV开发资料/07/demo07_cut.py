import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread("lena.png")  # 使用imread函数读取名为lena.png的图片
img_b = img  # 蓝色图像定义
img_b[:, :, 1] = 0  # 将绿色通道取消
img_b[:, :, 2] = 0  # 将红色通道取消
cv2.imshow('蓝色图像', img_b)  # 使用imshow函数展示蓝色图像
img = cv2.imread("lena.png")  # 使用imread函数读取名为lena.png的图片
img_g = img  # 绿色图像定义
img_g[:, :, 0] = 0  # 将蓝色通道取消
img_g[:, :, 2] = 0  # 将红色通道取消
cv2.imshow("绿色图像", img_g)  # 使用imshow函数展示绿色图像
img = cv2.imread("lena.png")  # 使用imread函数读取名为lena.png的图片
img_r = img  # 红色图像定义
img_r[:, :, 0] = 0  # 将蓝色通道取消
img_r[:, :, 1] = 0  # 将绿色通道取消
cv2.imshow('红色图像', img_r)  # 使用imshow函数展示红色图像
cv2.waitKey(0)
