import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:

    # 영상 프레임 읽기
    ret, frame = capture.read()
    # 이진화를 통해 흑백으로 바꿈
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    # 영상 출력
    cv2.imshow("VideoFrame", dst)
    # 키 누르면 종료
    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()

