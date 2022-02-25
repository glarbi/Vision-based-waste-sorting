import cv2
import os

vid = cv2.VideoCapture("../sorting_waste.mp4")

if (not vid.isOpened()):
	print ("file not found")
else:
	if not os.path.exists('data'):
		 os.makedirs('data')
			
	frame_count = vid.get(cv2.CAP_PROP_FRAME_COUNT) # get number of frames in the video
	print ("frame_count", frame_count)
	i=1
	
	while i<frame_count: # loop until arrived to the end of the video
		vid.set(1,i); # specify wich frame to get
		success, frame = vid.read()
		
		if (success):
			#cv2.imshow("Output", frame)
			#cv2.imwrite("./data/frame" + str(i) + '.png', frame)
			cv2.imwrite("./data/frame" + str(i) + '.png', frame)

	 #   if cv2.waitKey(1) & 0xFF == ord('q'):
	 #       break
		i += 100 # get 1 frame for every 100 frames of video

	vid.release()
	#cv2.destroyAllWindows()
