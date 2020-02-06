import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)
while(1):
    # читаем кадр
    _, frame = cap.read()
    # white_frame = np.zeros([])
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # показываем изображение grayscale
    cv2.imshow('image_gray', gray_frame)
    # вычисляем границы
    gray_edges = cv2.Canny(gray_frame, threshold1=50, threshold2=150, apertureSize=3, L2gradient=False)
    # показываем границы
    cv2.imshow('Canny_gray', gray_edges)
    # изображение, где будем рисовать найденные линии
    lines_gray= np.copy(gray_frame)
    # собственно ищем линии
    lines = cv2.HoughLines(gray_edges, 1, np.pi / 180, 150, None, 0, 0)
    
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(lines_gray, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    
    # linesP = cv2.HoughLinesP(gray_edges, 1, np.pi / 180, 50, None, 50, 10)
    
    # if linesP is not None:
    #     for i in range(0, len(linesP)):
    #         l = linesP[i][0]
    #         cv2.line(lines_gray, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
    
    cv2.imshow('Lines', lines_gray)
    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break
    
# findContours для именно кнтуров - надо??