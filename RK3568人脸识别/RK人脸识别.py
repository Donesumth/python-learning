import cv2
import cv2 as cv
import numpy as np
from PIL import Image
import os
import json

# 收集图像
# 训练模型
# 和名字映射对应
dataset_path = 'dataset'  # 存放收集的人脸信息目录
trainer_path = 'trainer'  # 存放训练好的模型
names_mapping_path = 'names_mapping.json'


def input_name():
    # 读取已存在的用户Id
    if os.path.exists(names_mapping_path):
        with open(names_mapping_path, 'r') as f:
            names_mapping = json.load(f)
    else:
        names_mapping = {}
    # {"zhangsan":1,"lisi":2}
    # 自动分配ID
    new_id = max(names_mapping.values(), default=0) + 1
    name = input(f"请输入名字(ID将自动分配为{new_id}):")
    names_mapping[name] = new_id
    with open(names_mapping_path, 'w') as f:
        json.dump(names_mapping, f)
    return new_id


def capture_faces(face_id):
    '''
    捕获人脸信息
    :param face_id:
    :return:
    '''
    # 打开摄像头
    cam = cv.VideoCapture(0)
    if not cam.isOpened():
        print("错误：无法打开摄像头。")
        return
    # 设置摄像头的高度和宽度
    cam.set(3, 640)
    cam.set(4, 480)
    # 加载人脸的调试模型
    face_detector = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    print("\n[信息] 正在初始化人脸捕捉。看着摄像头并等待......")

    # 初始化样本计数
    count = 0
    detect_interval = 5
    frame_count = 0
    while True:
        ret, img = cam.read()
        if not ret:
            print("抓取帧失败")
            break
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #BGRA -> BGR
        # 每隔一定的帧数进行一次人脸检测
        if frame_count % detect_interval == 0:
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 画出检测到的人脸矩形
                count += 1
                # 保存捕获到的人脸信息
                cv.imwrite(os.path.join(dataset_path, f"User.{face_id}.{count}.jpg"), gray[y:y + h, x:x + w])
                if count >= 10:
                    break
        cv.imshow('image', img)
        frame_count += 1
        k = cv.waitKey(1) & 0xff
        if k == 27 or count >= 10:
            break
    cam.release()
    cv.destroyAllWindows()


def train_model():
    '''
    训练人脸识别模型并保存
    :return:
    '''
    # 创建LBPH面部识别器
    recognizer = cv.face.LBPHFaceRecognizer_create()
    detector = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path):
        '''
        从指定路径获取图像和标签
        :param path:
        :return:
        '''
        imagePath = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
        faceSamples = []
        ids = []
        for imagePath in imagePath:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        return faceSamples, ids

    print("\n[信息] 正在训练人脸识别模型。请稍等.....")
    faces, ids = getImagesAndLabels(dataset_path)
    recognizer.train(faces, np.array(ids))
    recognizer.write(os.path.join(trainer_path, 'trainer.yml'))
    print(f"\n[信息] {len(np.unique(ids))} 张人脸已训练。程序结束")

def recognize_faces():
    '''

    :return:
    '''
    recognizer=cv.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    #读取训练好的模型
    cascadePath='haarcascade_frontalface_default.xml'
    fastcache=cv.CascadeClassifier(cascadePath)
    font=cv.FONT_HERSHEY_SIMPLEX
    if os.path.exists(names_mapping_path):
        with open(names_mapping_path,'r') as f:
            names_mapping=json.load(f)
        names={v:k for k,v in names_mapping.items()}
    else:
        print("错误：未找到名字映射文件。")
        return
    cam=cv.VideoCapture(0)
    if not  cam.isOpened():
        print("错误：无法打开摄像头。")
        return
    cam.set(3, 640)
    cam.set(4, 480)
    minW=0.1*cam.get(3)
    minH=0.1*cam.get(4)

    while True:
        ret,img=cam.read()
        if not ret:
            print("抓取帧失败")
            break
        gray=cv.cvtColor(img,cv.COLOR_BGRA2GRAY)

        faces=fastcache.detectMultiScale(gray,
                                         scaleFactor=1.2,
                                         minNeighbors=5,
                                         minSize=(int(minW),int(minH)))
        for (x,y,w,h ) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,confidence=recognizer.predict(gray[y:y+h,x:x+w])
            if confidence<100:
                name=names.get(id,"未知")
            else:
                name="未知"
            cv.putText(img,name,(x+5,y-5),font,1,(255,255,255),2)
        cv2.imshow('camera',img)
        k=cv.waitKey(10)&0xff
        if k==27:
            break
    cam.release()
    cv.destroyAllWindows()

def main():
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)
    if not os.path.exists(trainer_path):
        os.makedirs(trainer_path)
    while True:
        print("请选择一个操作：")
        print("1. 数据采集")
        print("2. 训练模型")
        print("3. 实时识别")
        print("4. 退出")
        choice = input("请输入你的选择：")
        if choice == '1':
            # 输入姓名
            face_id = input_name()
            capture_faces(face_id)
        elif choice == '2':
            train_model()
        elif choice == '3':
            recognize_faces()

        elif choice == '4':
            print("退出程序")
            break

        else:
            print("无效的选择，请重试。")


if __name__ == '__main__':
    main()