import serial

serial_port ='/dev/cu.usbmodem1411'
baud_rate = 9600 #In arduino, Serial.begin(baud_rate)
write_to_file_path = "n5_4.txt"

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = str(ser.readline())
    line = str(line.decode("utf-8")) #ser.readline returns a binary, convert to string
    print(line)
    output_file.write(line)
    

