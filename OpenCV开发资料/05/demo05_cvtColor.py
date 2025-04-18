import cv2  # opencv的缩写为cv2，导入opencv

img = cv2.imread("lena.png")  # 使用imread函数读取名为lena.png的图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 读取的图片转换成黑白的
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 读取的图片转换成HSV
cv2.imshow('gray', gray)  # 使用imshow函数将转换之后的图片进行转换
cv2.imshow('hsv', hsv)
cv2.waitKey(0)  # 等待按键的按下
cv2.destroyAllWindows()  # 关闭窗口，清除程序所占用的内存

