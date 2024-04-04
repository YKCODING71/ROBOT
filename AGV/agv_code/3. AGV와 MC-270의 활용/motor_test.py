from pymycobot.myagv import MyAgv
import time

MA = MyAgv('/dev/ttyACM#', 115200)

# forward
MA.go_ahead(40)
time.sleep(3)

# backward
MA.retreat(40)
time.sleep(3)

# turn left
MA.pan_left(40)
time.sleep(3)

# turn right
MA.pan_right(40)
time.sleep(3)

# clockwise
MA.clockwise_rotation(40)
time.sleep(3)

# counterclockwise
MA.counterclockwise_rotation(40)
time.sleep(3)

MA.stop()