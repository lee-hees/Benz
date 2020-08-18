import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:

    # 영상 프레임 읽기
    ret, frame = capture.read()

    dst = frame.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)

    for i in corners:
        cv2.circle(dst, tuple(i[0]), 3, (0, 0, 255), 2)
    # 영상 출력
    cv2.imshow("VideoFrame", dst)
    # 키 누르면 종료
    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()

