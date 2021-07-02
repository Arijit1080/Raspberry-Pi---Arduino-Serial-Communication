import serial
import time

arduino_serial = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
arduino_serial.flush()
while True:
    arduino_serial.write(b"I am Raspberry Pi!\n")
    line = arduino_serial.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)
