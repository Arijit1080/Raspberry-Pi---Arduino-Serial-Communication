import serial
arduino_serial = serial.Serial(port="/dev/ttyAMA0", baudrate=9600, timeout=.1)
while True:
    if(arduino_serial.in_waiting >0):
        line = arduino_serial.readline()
        print(line)