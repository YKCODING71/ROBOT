from PyQt5.QtWidgets import *      # PyQt5.QtWidgets으로 부터 QApplication, QStyleFactory, QMainWidow, QWidget, QGridLayout 클래스
import sys
				
from myjoystick import MyJoystick
			
def cbJoyPos(joystickPosition) :   # 콜백 함수, 조이스틱 위치값을 인자로 받아 출력
	print(joystickPosition)          # 좌표값은 X, Y축에 대하여 -1에서 1 사이

# Create main application window
app = QApplication([])             # 응용프로그램 객체와 주 윈도우 실행
app.setStyle(QStyleFactory.create("Cleanlooks"))
mw = QMainWindow()
mw.setWindowTitle('RC Car Joystick')
mw.setGeometry(100, 100, 300, 200)

# Create and set widget layout
# Main widget container
cw = QWidget()                     # 주 윈도우에 놓일 위젯 생성
ml = QGridLayout()
cw.setLayout(ml)
mw.setCentralWidget(cw)

# Create joystick
joystick = MyJoystick(cbJoyPos)    # 조이스틱 인스턴스 생성
ml.addWidget(joystick,0,0)

mw.show()                          # 윈도우를 화면에 표시

# Start Qt event loop 
sys.exit(app.exec_())              # 마우스, 키보드, 타이머 등 처리