from .tracker import Tracker
import time


f = open("config/config.txt","r")
interval = int(f.readline().split("=")[1].strip())
print(interval)
f.close()

t = Tracker()
while 1:
	t.increment()
	print(str(t))
	t.save_to_file()
	time.sleep(interval)