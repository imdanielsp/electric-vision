import cv2
from stereovision.calibration import StereoCalibrator
from stereovision.ui_utils import calibrate_folder

input_folder = 'pictures/'


class CalibrationInfo:
    input_files = [
        input_folder + '1-1.jpg',
        input_folder + '1-2.jpg',
        input_folder + '2-1.jpg',
        input_folder + '2-2.jpg',
        input_folder + '3-1.jpg',
        input_folder + '3-2.jpg',
        input_folder + '4-1.jpg',
        input_folder + '4-2.jpg',
    ]

    def __init__(self, rows=9, columns=6, square_size=2.3,
                 output_folder="calibration", show_chessboards=False):
        self.rows = rows
        self.columns = columns
        self.square_size = square_size
        self.output_folder = output_folder
        self.show_chessboards = show_chessboards


calibrate_folder(CalibrationInfo())
