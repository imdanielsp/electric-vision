from stereovision.stereo_cameras import StereoPair, CalibratedPair
from stereovision.calibration import StereoCalibration
from stereovision.blockmatchers import StereoBM


sp = StereoPair([0, 0])

block_matcher = StereoBM()

camera_pair = CalibratedPair(None,
                             StereoCalibration(input_folder='calibration/'),
                             block_matcher)
rectified_pair = camera_pair.calibration.
