import cv2

video_capture = cv2.VideoCapture("test.mp4")  # 使用VideoCapture函数读取名为test.mp4的视频文件
frame_num = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)  # 使用video_capture.get函数获取总帧数
print("总帧数为 %f" % frame_num)
fps = video_capture.get(cv2.CAP_PROP_FPS)  # ==>使用video_capture.get函数获取帧率
print("帧率为 %f" % fps)
width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)  # ==>使用video_capture.get函数获取视频宽度
print("视频宽度为 %f" % width)
height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # ==>使用video_capture.get函数获取视频高度
print("视频高度为 %f" % height)
