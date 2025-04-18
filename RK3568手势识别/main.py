#导入OPenCv
import cv2 as cv
from handutil import HandDetector
import numpy as np


def main():
    #打开摄像头
    cap=cv.VideoCapture(0)
    #创建一个手势识别对象
    detector=HandDetector()

    # 6张手的图片，分别代表0~5
    finger_img_list =[
        'fingers/0.png',
        'fingers/1.png',
        'fingers/2.png',
        'fingers/3.png',
        'fingers/4.png',
        'fingers/5.png',
    ]
    finger_list= []
    for fi in finger_img_list:
        i = cv.imread(fi)
        finger_list.append(i)
    else:
        print(f"Warning: Failed to load image {fi}")

    #定义指尖列表,从大拇指到小拇指指尖
    tip_ids=[4,8,12,16,20]
    while True:
        #读取摄像头的帧
        success,img=cap.read()
        #通常情况下要修正摄像头的水平反转
        cv.flip(img,1)
        #判断是否读取到摄像头帧画面
        if success:
            #将识别到的手势进行识别然后在显示
            img=detector.find_hands(img)
            #获取手势数据
            lmslist = detector.find_positions(img)
            if len(lmslist) > 0:
                fingers = []  # 初始化 fingers 列表
                print('lmslist:', lmslist)
                print('lmslist.shape:', np.array(lmslist).shape)  # (21, 3)
                for tid in tip_ids:
                    x,y= lmslist[tid][1],lmslist[tid][2]
                    cv.circle(img,(x,y),10,(0,255,0),cv.FILLED)

                    # 如果是大拇指，如果大拇指指尖x位置大于大拇指第二关节的位置，则认为大拇指打开，否则认为大拇指关闭
                    if tid==4:
                        #根据食指和中指的位置判断左手右手
                        if lmslist[8][1] < lmslist[12][1]:
                            # 右手
                            if lmslist[tid][1] < lmslist[tid-1][1]:
                                fingers.append(1)
                            else:
                                fingers.append(0)
                        else:
                            #左手
                            if lmslist[tid][1] > lmslist[tid-1][1]:
                                fingers.append(1)
                            else:
                                fingers.append(0)
                    #如果是其他手指，如果这些手指的指尖的y位置大于第二关节的位置，则认为这个手指打开，否则认为这个手指关闭
                    else:
                        if lmslist[tid][2] < lmslist[tid - 2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                    #fingers是这样一个列表，5个数据，0代表一个手指关闭，1代表一个手指打开
                    #判断有几个手指打开
                    cnt = fingers.count(1)

                    # 找到对应的手势图片并显示
                    finger_img = finger_list[cnt]
                    w,h,c=finger_img.shape
                    img[0:w,0:h]=finger_img

                    print('cnt:', cnt)

            cv.imshow('Image',img)
        #通过键盘上的某个按键退出摄像头
        k=cv.waitKey(1)
        if k==ord('q'):
            break
    #释放资源
    cap.release()
    cv.destroyAllWindows()

if __name__=='__main__':
    main()
