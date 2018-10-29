from picamera import PiCamera
from time import sleep

camera = PiCamera()

#only view no photo
#camera.start_preview()
#sleep(15)
#camera.stop_preview()


#able to rotate camera if needed 


#taking one photo
#camera.start_preview()
#sleep(5)
#camera.capture('/home/pi/pi/camera/images.jpg')
#camera.stop_preview()

#take five photos
camera.start_preview()
for i in range(5):
	sleep(5)
	camera.capture('/home/pi/pi/camera/images%s.jpg' % i)
camera.stop_preview()

camera.start_preview()
camera.start_recording('/home/pi/pi/camera/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
