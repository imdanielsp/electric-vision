import serial
import time


class MotorController:
    def __init__(self, port, baud=9600, timeout=0.5):
        self._sp = serial.Serial(port, baud)
        self.handshake()

    def handshake(self):
        ok = False
        while not ok:
            time.sleep(2)
            print("Writing I...")
            self._sp.write(b'I')
            time.sleep(2)
            print("Reading...")
            res = self._sp.read()
            print("Got: %s" % res)
            if res == b'A':
                ok = True

    def send(self, motor_on):
        self._sp.write('1' if motor_on else '0')
