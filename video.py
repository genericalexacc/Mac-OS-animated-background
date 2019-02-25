import cv2
import sys

vidcap = cv2.VideoCapture(sys.argv[1]) #YOU CAN MANUALLY CHANGE TO A GIF OR VIDEO OF YOUR CHOICE
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./images/frame%d.jpg" % count, image)
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
