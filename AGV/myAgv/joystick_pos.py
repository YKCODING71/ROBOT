from PyQt5.QtWidgets import *
import sys
				
from myjoystick import MyJoystick
			
def cbJoyPos(joystickPosition) :
	print(joystickPosition)

# Create main application window
app = QApplication([])
app.setStyle(QStyleFactory.create("Cleanlooks"))
mw = QMainWindow()
mw.setWindowTitle('RC Car Joystick')
mw.setGeometry(100, 100, 300, 200)

# Create and set widget layout
# Main widget container
cw = QWidget()
ml = QGridLayout()
cw.setLayout(ml)
mw.setCentralWidget(cw)

# Create joystick
joystick = MyJoystick(cbJoyPos)
ml.addWidget(joystick,0,0)

mw.show()

# Start Qt event loop 
sys.exit(app.exec_())