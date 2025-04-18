import cv2  # opencv的缩写为cv2，导入opencv

cap = cv2.VideoCapture("test.mp4")  # 使用VideoCapture函数读取名为test.mp4的视频文件
fps = cap.get(cv2.CAP_PROP_FPS)  # 使用video_capture.get函数获取帧率
while True:  # while循环，能持续播放读取到的视频
    ret, frame = cap.read()  # 使用read()函数读取图像的帧，一次循环读取一帧
    cv2.imshow("video", frame)  # 使用imshow()函数对读取到的帧进行显示
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):  # 设置视频播放完成和按下q键退出
        break
cap.release()  # 释放cap
cv2.destroyAllWindows()  # 关闭窗口，清除程序所占用的内存
