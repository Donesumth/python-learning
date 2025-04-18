import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread('lena.png', 1)  # flags参数为1，返回彩色图像
res = cv2.resize(img, (256, 256))  # 使用resize()函数将高度宽度固定为256
cv2.imshow('固定高度宽度图', res)  # 使用cv2.imshow()函数进行缩放图像的展示
res2 = cv2.resize(res, None, fx=2, fy=2)  # 使用resize()函数将res图像放大两倍
cv2.imshow('等比例放大图', res2)  # 使用cv2.imshow()函数进行缩放图像的展示
cv2.waitKey(0)  # 等待下一次按键按下
