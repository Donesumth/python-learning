import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lena.png')  # 使用imread函数读取名为lena.png的图片
cv2.imshow('origin', img)  # 使用imshow函数展示原图

replicate = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)  # 使用copyMakeBorder函数对边缘使用复制法填充
cv2.imshow('replicate', replicate)  # 使用imshow函数展示处理过的图像

reflect = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT)  # 使用copyMakeBorder函数对边缘使用反射法填充
cv2.imshow('reflect', reflect)  # 使用imshow函数展示处理过的图像

reflect101 = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)  # 使用copyMakeBorder函数对边缘使用反射法填充
cv2.imshow('reflect101', reflect101)  # 使用imshow函数展示处理过的图像

wrap = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_WRAP)  # 使用copyMakeBorder函数对边缘使用外包装法填充
cv2.imshow('wrap', wrap)  # 使用imshow函数展示处理过的图像

constant = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT,
                              value=(255, 255, 255))  # 使用copyMakeBorder函数对边缘使用常数填充，这里为白色
cv2.imshow('constant', constant)  # 使用imshow函数展示处理过的图像
cv2.waitKey(0)  # 等待按键的按下
