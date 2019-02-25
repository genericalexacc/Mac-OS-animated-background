from time import sleep
from appscript import app, mactypes

counter = 0

while(True):
	sleep(0.1)
	file = './images/frame' + str(counter) + '.jpg'
	print(file)
	try:
		app('Finder').desktop_picture.set(mactypes.File(file))
	except Exception as e:
		print(e)
	counter+=1
	if counter==12:
		counter=0
