import serial

ser = serial.Serial("COM4", 9600)

dataline = ser.readline()
dataline = dataline.decode()

print(dataline)