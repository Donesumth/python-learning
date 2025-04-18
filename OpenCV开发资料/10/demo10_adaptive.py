import cv2  # opencv的缩写为cv2，导入opencv

img_gray = cv2.imread('english.bmp', 0)  # 使用imread函数读取名为english.bmp的图片,且读取的是灰度图
cv2.imshow("img_gray", img_gray)  # 使用imshow函数展示灰度图
# 调用adaptiveThreshold函数进行自适应阈值分割
# 满足条件的像素点设置为255，及最大亮度
# 自适应阈值算法类型这里设置为cv2.ADAPTIVE_THRESH_MEAN_C
# 二值化方法这里设置为cv2.THRESH_BINARY
# 分成的区域设置为11，常数C为4
img_adaptive = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
cv2.imshow("img_adaptive", img_adaptive)  # 使用imshow函数展示阈值分割之后的图像
cv2.waitKey(0)  # 等待按键的按下
