from time import sleep
import ax12 as ax12
import sys
sys.path.append("../")

servos= ax12.Ax12();

while (1):
	servos.move(9,500)
	time.sleep(2)
	servos.move(9,800)
	time.sleep(2)