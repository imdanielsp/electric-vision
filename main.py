from stereovision.stereo_cameras import StereoPair, CalibratedPair
from stereovision.calibration import StereoCalibration
from stereovision.blockmatchers import StereoBM
import numpy as np

from MotoControl import MotorController

DEVICES_ID = [2, 0]

ply_header = (
'''ply
format ascii 1.0
element vertex {vertex_count}
property float x
property float y
property float z
end_header
'''
)

x_ply_header = (
'''ply
format ascii 1.0
element vertex {vertex_count}
property float z
end_header
'''
)


def list_to_ply(numbers, output_file):
    numbers = np.hstack([numbers])
    with open(output_file, 'w') as outfile:
        outfile.write(ply_header.format(vertex_count=len(numbers)))
        np.savetxt(outfile, numbers, '%f %f %f')


def z_to_ply(numbers, output_file):
    numbers = np.hstack([numbers])
    with open(output_file, 'w') as outfile:
        outfile.write(x_ply_header.format(vertex_count=len(numbers)))
        np.savetxt(outfile, numbers, '%f %f %f')


def run():
    motor_controller = MotorController('/dev/cu.usbmodem14211')
    sp = StereoPair(DEVICES_ID)
    block_matcher = StereoBM()

    camera_pair = CalibratedPair(None,
                                 StereoCalibration(input_folder='calibration/'),
                                 block_matcher)

    current_value = None
    last_size = None
    i = 0
    while True:
        frames_single_img = sp.get_frames()
        points = camera_pair.get_point_cloud(frames_single_img)
        points = points.filter_infinity()

        number = []
        for level1 in points.coordinates:
            if not level1[2] == 512:
                number.append([0.0, 0.0, level1[2]])
        number_size = len(number)
        if last_size:
            current_value = (number_size + last_size) / 2
            # print current_value
        last_size = number_size
        i += 1

        motor_state = False
        if not current_value >= 3000:
            print current_value
            motor_state = True
        motor_controller.send(motor_state)


if __name__ == '__main__':
    run()
