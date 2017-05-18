import sys
from time import sleep,time
sys.path.append("..")
import ax12 as ax12

if __name__=="__main__":
	while true:
		ax12.move(11, 10)
		time.sleep(2)
		ax12.move(11, 30)
		time.sleep(2)
			

