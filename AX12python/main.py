import time
import ax12 as ax12
import sys
sys.path.append("../")

servos= ax12.Ax12();
servos.__init__();

while (1):
	servos.move(32,500)
	time.sleep(2)
	servos.move(32,800)
	time.sleep(2)