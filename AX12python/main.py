from time import sleep
from ax12 import ax12
import sys
sys.path.append("../")

servos= ax12.Ax12();

while true:
	servos.move(9,500)
	time.sleep(2)
	servos.move(9,800)
	time.sleep(2)