import cv2
from stereovision.calibration import StereoCalibrator

image = 'chessboard.png'

height, width = cv2.imread(image).shape[:2]
calibrator = StereoCalibrator(9, 6, 2.3, (width, height))

img_left, img_right = cv2.imread(image), cv2.imread(image)
calibrator.add_corners((img_left, img_right))

calibration = calibrator.calibrate_cameras()

calibration.export('calibration/')
