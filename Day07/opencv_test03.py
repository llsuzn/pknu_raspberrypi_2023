# OpenCV test
import  cv2
from picamera2 import Picamera2

cam = Picamera2()
cam.preview_configuration.main.size=(800,600)
cam.preview_configuration.main.format='RGB888'
cam.preview_configuration.align()

cam.configure('preview')
cam.start()

while True:
    frame = cam.capture_array()

    frame_blur = cv2.blur(frame, (10,10))

    cv2.imshow('piCam',frame_blur)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()    
