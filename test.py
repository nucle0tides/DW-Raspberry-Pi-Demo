"""
	The first test script! 
	Right click to paste
	Use ctrl + o to save 
	Use ctrl + x to exit the text editor
"""

import time
import picamera

#create an instance of our camera 
camera = picamera.PiCamera() 
#set the resulotion 
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
time.sleep(2)
#capture the image
camera.capture('test.jpg')
#close the camera
camera.close()