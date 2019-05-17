import serial.tools.list_ports

def findPorts():
    ports = serial.tools.list_ports.comports()
    return ports


def findArduino(ports_found):

    com_found = 'None'
    port_count = len(ports_found)

    for i in range(0,port_count):
        port = ports_found[i]
        string_port = str(port)

        if 'Serielles' or 'Arduinio' in string_port:
            split_port = string_port.split();
            com_found = split_port[0]

    return com_found

my_ports = findPorts()
arduino_port = findArduino(my_ports)

if arduino_port == 'None':
    print("Error - port not found")

else:
    print(f"Arduino Port: {arduino_port}")

ser = serial.Serial(arduino_port, baudrate = 9600, timeout = 1)

while 1:

    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)

