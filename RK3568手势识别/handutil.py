import cv2 as cv
import mediapipe as mp

class HandDetector:
    #手势识别控制类
    def __init__(self, mode=False, max_hands=2, complexity=1, detection_con=0.5, track_con=0.5):
        '''
        手势识别初始化
        :param mode: 是否为静态图片。默认为False(不是静态图片)
        :param max_hands: 最多检测几只手 默认为2
        :param complexity: 模型复杂度 默认为1
        :param detection_con: 最小检测置信度 默认为0.5
        :param track_con: 最小追踪置信度 默认为0.5
        '''
        self.mode = mode
        self.max_hands = max_hands
        self.complexity = complexity
        self.detection_con = detection_con
        self.track_con = track_con
        self.hands = mp.solutions.hands.Hands(static_image_mode=mode,
                                              max_num_hands=2,
                                              model_complexity=1,
                                              min_detection_confidence=0.5,
                                              min_tracking_confidence=0.5)

    def find_hands(self, img):
        '''
        检测手势
        :param img: 视频帧图片
        :return: 处理过的视频帧图片
        '''
        # 需要把BGR格式转换为RGB格式 才能传入process()方法中
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        # 处理图片 检测是否有手势(注意参数必须是RGB格式)
        self.results = self.hands.process(imgRGB)
        # print(self.results.multi_hand_landmarks)
        # 只有检测到手，才进行绘制
        if self.results.multi_hand_landmarks:  # != None
            # 遍历每只手 注意self.results.multi_hand_landmarks最多可能为2
            for handlms in self.results.multi_hand_landmarks:
                # 绘制手势
                # 参数1 image。在哪张图片上绘制
                # 参数2 landmark_list。手势列表
                # 参数3 connections
                mp.solutions.drawing_utils.draw_landmarks(imgRGB,
                                                          handlms,
                                                          mp.solutions.hands.HAND_CONNECTIONS)

        # 把RGB格式转回到BGR格式
        img = cv.cvtColor(imgRGB, cv.COLOR_RGB2BGR)

        return img

    #定义一个方法，方法参数接收一个摄像头的帧画面，然后分析出手的数据
    def find_positions(self,img,hand_no=0):
        """
        获取手势数据
        :param img: 视频中的图片
        :param hand_no: 手编号
        :return:
        """
        self.lmslist=[]
        #检测到手才去获取数据
        if self.results.multi_hand_landmarks:
            hand=self.results.multi_hand_landmarks[hand_no]
            #遍历手的ID和关节数据
            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmslist.append([id, cx, cy])

        return self.lmslist



