import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:

    # 영상 프레임 읽기
    ret, src = capture.read()

    dst = src.copy()
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 5000, 1500, apertureSize = 5, L2gradient = True)
    lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 150, srn = 100, stn = 200, min_theta = 0, max_theta = np.pi)

    for i in lines:
        rho, theta = i[0][0], i[0][1]
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a*rho, b*rho

        scale = src.shape[0] + src.shape[1]

        x1 = int(x0 + scale * -b)
        y1 = int(y0 + scale * a)
        x2 = int(x0 - scale * -b)
        y2 = int(y0 - scale * a)

        cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.circle(dst, (x0, y0), 3, (255, 0, 0), 5, cv2.FILLED)

    # 영상 출력
    cv2.imshow("VideoFrame", dst)
    # 키 누르면 종료
    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()

