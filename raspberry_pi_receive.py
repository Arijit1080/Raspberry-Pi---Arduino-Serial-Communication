import serial
ser = serial.Serial('/dev/ttyAMA0', 9600)
while 1:
    if(ser.in_waiting >0):
        line = ser.readline()
        print(line)