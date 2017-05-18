import sys
from time import sleep,time
sys.path.append("..")
import ax12 as ax12

a = ax12.Ax12()
while(1):
	a.move(11, 10)
	time.sleep(2)
	a.move(11, 30)
	time.sleep(2)

			

