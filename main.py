import math
import cv2
import numpy as np

# 判断七色花
def detectFlower(img):
    # 预处理
    # 颜色过滤
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # --------------------------------------------#
    # -------------------a花朵检测-----------------#
    a_min = np.array([151, 56, 176])
    a_max = np.array([166, 206, 255])

    # 提取指定色区域
    mask = cv2.inRange(hsv, a_min, a_max)
    mask = cv2.medianBlur(mask, 9)  # 中值滤波
    # cv2.imshow('mask_Blur', mask)

    # 轮廓检测
    binary, contours2, hierarchy2 = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt2 in contours2:
        center, radius = cv2.minEnclosingCircle(cnt2)
        area = cv2.contourArea(cnt2)

        rate = area / (math.pi * radius * radius)


        if radius > 100 and radius < 200 and rate>0.6:
            # print(rate)
            cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (203,203,255), 2)
            print('a')

    # --------------------------------------------#
    # -------------------b花朵检测-----------------#
    b_min = np.array([0, 159, 177])
    b_max = np.array([123, 251, 209])

    # 提取指定色区域
    mask = cv2.inRange(hsv, b_min, b_max)
    mask = cv2.medianBlur(mask, 9)  # 中值滤波
    # cv2.imshow('mask_Blur', mask)

    # 轮廓检测
    binary, contours2, hierarchy2 = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt2 in contours2:
        center, radius = cv2.minEnclosingCircle(cnt2)

        if radius < 30 and radius > 5:
            # print(radius)
            cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (0, 255, 255), 2)
            print('b')

    # --------------------------------------------#
    # -------------------h/c花朵检测-----------------#
    c_min = np.array([9, 49, 210])
    c_max = np.array([72, 255, 255])
    h_min = np.array([141, 106, 85])
    h_max = np.array([157, 255, 255])

    # 提取指定色区域
    mask1 = cv2.inRange(hsv, c_min, c_max)
    mask1 = cv2.medianBlur(mask1, 9)  # 中值滤波
    mask2 = cv2.inRange(hsv, h_min, h_max)
    mask2 = cv2.medianBlur(mask2, 9)  # 中值滤波

    # 轮廓检测
    binary, contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    binary, contours2, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours1:
        center, radius = cv2.minEnclosingCircle(cnt)

        if radius > 10 and radius < 100:
            # print(radius)
            if len(contours2) >3:
                cv2.circle(img, (int(center[0]), int(center[1])), int(radius*2.2), (128, 0, 0), 2)
                print('h')
            else:
                cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (0, 255, 255), 2)
                print('c')

    # --------------------------------------------#
    # -------------------d花朵检测-----------------#
    d_min = np.array([163, 96, 0])
    d_max = np.array([255, 255, 255])

    # 提取指定色区域
    mask = cv2.inRange(hsv, d_min, d_max)
    mask = cv2.medianBlur(mask, 9)  # 中值滤波
    # cv2.imshow('mask_Blur', mask)

    # 轮廓检测
    binary, contours2, hierarchy2 = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt2 in contours2:
        center, radius = cv2.minEnclosingCircle(cnt2)
        # area = cv2.contourArea(cnt2)
        # print(radius)

        if radius > 100 and radius < 200:
            # print(radius)
            cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (0, 0, 255), 2)
            print('d')

    # --------------------------------------------#
    # -------------------f花朵检测-----------------#
    f_min = np.array([9, 49, 210])
    f_max = np.array([72, 255, 255])

    # 提取指定色区域
    mask = cv2.inRange(hsv, f_min, f_max)
    mask = cv2.medianBlur(mask, 9)  # 中值滤波
    # cv2.imshow('mask_Blur', mask)

    # 轮廓检测
    binary, contours2, hierarchy2 = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt2 in contours2:
        center, radius = cv2.minEnclosingCircle(cnt2)
        # area = cv2.contourArea(cnt2)
        # print(radius)

        if radius > 100 and radius < 200:
            # print(radius)
            cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (0, 255, 255), 2)
            print('f')

    # --------------------------------------------#
    # -------------------g花朵检测-----------------#
    g_min = np.array([141, 106, 85])
    g_max = np.array([157, 255, 255])

    # 提取指定色区域
    mask = cv2.inRange(hsv, g_min, g_max)
    mask = cv2.medianBlur(mask, 9)  # 中值滤波
    # cv2.imshow('mask_Blur', mask)

    # 轮廓检测
    binary, contours2, hierarchy2 = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt2 in contours2:
        center, radius = cv2.minEnclosingCircle(cnt2)
        # area = cv2.contourArea(cnt2)
        # print(radius)

        if radius > 140 and radius < 200:
            # print(radius)
            cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (128,0,128), 2)
            print('g')


    return img

if __name__ == '__main__':
    path = r'1.jpg'
    # 1 调用图片
    # Using cv2.imread() method
    img = cv2.imread(path)

    # 2 识别
    img_out = detectFlower(img)

    cv2.imshow('img', img_out)
    cv2.waitKey(0)
