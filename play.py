from time import sleep
from appscript import app, mactypes

counter = 0

while(True):
	sleep(0.1)
	file = 'frame' + str(counter) + '.jpg'
	print(file)
	app('Finder').desktop_picture.set(mactypes.File(file))
	counter+=1
	if counter==12:
		counter=0
