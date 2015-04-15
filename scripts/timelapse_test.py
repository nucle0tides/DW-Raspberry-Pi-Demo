import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (1280, 720)
time.sleep(1) # Camera warm-up time
	for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
        print('Captured %s' % filename)
        # Capture one image a minute
        #decrease the time.sleep argument to take more images
        time.sleep(3)
        #this conditional will stop the iterator once 60 images have been taken, this can be changed too if you want. 
        if i == 59:
            break
