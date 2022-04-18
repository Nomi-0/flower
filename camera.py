import cv2

from main import detectFlower

# 保存截图
def get_img_from_camera_net(folder_path):
    cap = cv2.VideoCapture("rtsp://192.168.1.23:554/user=admin&password=&channel=1&stream=0.sdp?")  # 获取网络摄像机

    i = 1
    while i < 10:
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        print(str(i))
        cv2.imwrite(folder_path  + "/" + str(i) + '.jpg', frame)  # 存储为图像
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        i += 1
    cap.release()
    cv2.destroyAllWindows()

# 读取视频 并检测
def video():
    cap = cv2.VideoCapture("rtsp://192.168.1.23:554/user=admin&password=&channel=1&stream=0.sdp?")  # 获取网络摄像机

    ret, frame = cap.read()
    while ret:
        ret, frame = cap.read()

        # img = detectFlower(frame)

        cv2.imshow("current frame", frame)
        # cv2.imwrite('frame.jpg', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()

# 测试
if __name__ == '__main__':
    # folder_path = r'C:/Users/HH/PycharmProjects/flower/e'
    # get_img_from_camera_net(folder_path)

    video()