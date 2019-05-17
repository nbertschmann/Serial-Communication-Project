import serial.tools.list_ports
portData = serial.tools.list_ports.comports()


for i, j in enumerate(portData):
    print(f"{i+1})", end = " ")
    print(j)

print(len(portData))


for i in range(0,len(portData)):
    print(i);

