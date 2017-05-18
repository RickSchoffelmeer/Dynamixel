import sys
from time import sleep,time
sys.path.append("..")
import ax12 as ax12

a = Ax12()
if __name__=="__main__":
	a.move(11, 10)
	time.sleep(2)
	a.move(11, 30)
	time.sleep(2)
			

