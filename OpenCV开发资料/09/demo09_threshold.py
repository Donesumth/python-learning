import cv2  # opencv的缩写为cv2，导入opencv

img_gray = cv2.imread('rose.jpg', 0)  # 使用imread函数读取名为lena.png的图片，且读取的是灰度图
cv2.imshow('origin', img_gray)  # 使用imshow函数展示原图
ret, binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)  # 阈值类型设置为THRESH_BINARY
cv2.imshow('binary', binary)  # 使用imshow函数展示阈值分割之后的图像
ret, binary_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)  # 阈值类型设置为THRESH_BINARY_INV
cv2.imshow('binary_inv', binary_inv)  # 使用imshow函数展示阈值分割之后的图像
ret, trunc = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)  # 阈值类型设置为THRESH_BINARY_INV
cv2.imshow('trunc', trunc)  # 使用imshow函数展示阈值分割之后的图像
ret, tozero = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)  # 阈值类型设置为THRESH_TOZERO
cv2.imshow('tozero', tozero)  # 使用imshow函数展示阈值分割之后的图像
ret, tozero_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)  # 阈值类型设置为THRESH_TOZERO_INV
cv2.imshow('tozero_inv', tozero_inv)  # 使用imshow函数展示阈值分割之后的图像
cv2.waitKey(0)  # 等待按键的按下
