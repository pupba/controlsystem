import cv2

def generate_frames(server):
    """영상 스트리밍 함수"""
    cap = cv2.VideoCapture(server)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    n_frames = 5  # 5개의 프레임을 한 번에 읽도록 설정
    while True:
        # 스트리밍 서버로부터 프레임 받아오기
        success, frames = cap.read(n_frames)
        if not success:
            break
        else:
            for frame in frames:
                # 영상을 jpg 포맷으로 인코딩하여 스트리밍
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (f"--frame\r\nContent-Type: image/jpeg\r\n\r\n{frame}\r\n").encode('utf-8')