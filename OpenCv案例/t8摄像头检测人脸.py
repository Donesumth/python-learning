import cv2

# 定义一个函数，用于检测图像中的人脸并绘制矩形框
def face_demo(img):
    # 使用cv2.flip翻转图像，1表示沿着x轴翻转（水平翻转）
    frame = cv2.flip(img, 1)

    # 将图像从BGR颜色空间转换为灰度图，用于人脸检测
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 加载Haar特征分类器，用于人脸检测
    # 这里的分类器文件通常是OpenCV自带的，也可以是自定义的
    faceCascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

    # 使用detectMultiScale方法在灰度图像中检测人脸
    # 参数1.15是缩放比例因子，用于在多尺度空间中检测
    faces = faceCascade.detectMultiScale(gray, 1.15)

    # 遍历检测到的所有人脸区域
    for (x, y, w, h) in faces:
        # 在原图img上绘制矩形框，参数分别为(x, y)为左上角坐标，(x+w, y+h)为右下角坐标
        # (0, 0, 255)是颜色（蓝色），2是线条粗细
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("faces",img)

# 初始化视频捕捉对象，0表示第一个摄像头
video = cv2.VideoCapture(0)
# 循环直到用户按下ESC键
while True:
    # 读取视频的下一帧
    retval, image = video.read()
    # 显示原始视频帧
    cv2.imshow("Video", image)
    # 调用face_demo函数处理当前帧，并在检测到的人脸周围绘制矩形
    face_demo(image)
    # 1ms的延迟，等待用户按键操作
    key = cv2.waitKey(1)
    # 如果用户按下ESC键（ASCII码为27），则退出循环
    if key == 27:
        break
# 释放视频捕捉对象，释放与之关联的资源
video.release()
# 销毁所有OpenCV创建的窗口
cv2.destroyAllWindows()
