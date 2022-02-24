import cv2
import os

vid = cv2.VideoCapture("../sorting_waste.mp4") #2
if (not vid.isOpened()):
	print ("file not found")
else:
	crntframe = 0 #3

	#4
	if not os.path.exists('data'):
		 os.makedirs('data')
	frame_count = vid.get(cv2.CAP_PROP_FRAME_COUNT) # get number of frames in the video
	print ("frame_count", frame_count)
	i=1
	#while True: #5
	while i<frame_count: # loop until arrived to the end of the video
		vid.set(1,i); # specify wich frame to get
		success, frame = vid.read() #6
		if (success):
			#cv2.imshow("Output", frame) #7
			#cv2.imwrite("./data/frame" + str(crntframe) + '.png', frame) #8
			cv2.imwrite("./data/frame" + str(i) + '.png', frame) #8
			#crntframe += 1 #9

		#10
	 #   if cv2.waitKey(1) & 0xFF == ord('q'):
	 #       break
		i += 100 # get 1 frame for every 100 frames of video

	vid.release() #11
	#cv2.destroyAllWindows()  #12

"""
1. import the cv2 library to work with images.

2. store the video in a variable. if we want to capture from a camera, we use VideoCapture(0) for the 1st cam, and
VideoCapture(1) for the 2nd cam, etc.

3.variable will be used in naming.

4.create 'data' file to place the frames in it.

5.start an inifine loop.

6.vid.read() return a tuple(boolean, image itself), so success will be used to store the boolean value to tell us wether
the read was successfull or not. and frame will store the image it self.

7.to show the frames in a window.

8.to create the image.png using frame ( store the frame in an image.png).

9.incrementing the value. so the images will have diffrent names.

10.to break the loop if the video ended or the user wants to end the process.

11.closes video file or capturing device.

12.to close all the windows.

"""
