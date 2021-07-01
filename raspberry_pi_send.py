import serial
import time

arduino_serial = serial.Serial(port="/dev/ttyAMA0", baudrate=9600, timeout=.1)
try:
        while True:
                x = input("Enter a character: ")
                arduino_serial.write(bytes(x, 'utf-8'))
except KeyboardInterrupt:
        arduino_serial.close()