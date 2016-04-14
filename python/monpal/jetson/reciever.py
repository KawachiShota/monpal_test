import serial, time
serA = serial.Serial('/dev/ttyTHS0', 115200)
serB = serial.Serial('/dev/ttyTHS1', 115200)

while True:
    lineA = serA.read(8)
    print lineA
    time.sleep(0.1)

    lineB = serB.read(8)
    print lineB
    time.sleep(0.1)


serA.close()
serB.close()
