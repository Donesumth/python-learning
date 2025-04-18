import cv2

# 读取图像文件 "eye.jpg"
img = cv2.imread("eye.jpg")

# 加载识别眼睛的Haar级联分类器
# 级联分类器文件 "haarcascade_eye.xml"
faceCascade = cv2.CascadeClassifier("data/haarcascade_eye.xml")

# 使用级联分类器检测图像中的所有眼睛
# 参数解释：
# minNeighbors: 每个候选矩形至少应有多少个邻居，以保留此矩形。50表示需要较高的置信度
eyes = faceCascade.detectMultiScale(img, scaleFactor=1.15, minNeighbors=50)

# 遍历检测到的所有眼睛区域
for x, y, w, h in eyes:
    # 在原始图像上绘制矩形框标记检测到的眼睛区域
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 使用 OpenCV 显示图像窗口，展示带有矩形框的图像
cv2.imshow("img", img)
# 等待用户按键，保持窗口打开
cv2.waitKey()
# 关闭所有 OpenCV 窗口
cv2.destroyAllWindows()