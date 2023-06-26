# OpenCV test(캡처)
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

    qr = cv2.QRCodeDetector()
    data, box, str_qrcode = qr.detectAndDecode(frame)

    print(data)

    cv2.imshow('piCam',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()    
