import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import io
import base64

fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], 'r-')
def update(frame):
    # 애니메이션 업데이트 함수 정의
    xdata.append(frame)
    ydata.append(frame * frame)
    line.set_data(xdata, ydata)
    plt.title(f'Time: {frame}')  # 시간을 애니메이션의 제목으로 출력
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    return graphic

def makeRadar():
    ani = FuncAnimation(fig, update, frames=range(10), blit=True)
    plt.close(fig)  # 이미지 파일로 저장하기 위해 창을 닫음
    return ani.to_jshtml()