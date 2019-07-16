import sys
import serial
#import keyboard
#import pynput.keyboard as kb

print("modules start")
#print(kb.__file__)
print(serial.__file__)
print("modules end")

try:
    # open the serial port; only do this once as most arduinos reset when the serial port is opened
    ser = serial.Serial('/dev/ttyACM0', baudrate=9600)
    # e.g. remove remains of Arduino bootloader or old data while the application was not running
    # not sure yet if it's 100% reliable; robin's approach is probably safer
    ser.flushInput()

    while True:
        # check if bytes received
        numBytes = ser.inWaiting()
        if(numBytes > 0):
            serBytes = ser.readline()
            print(serBytes)
            # open file for binary (!) appending; not using binary results in
            # 1) error telling you 'must be str, not bytes'
            # 2) convering using str(ser_bytes) results in unwanted quotation marks in the file (as shown in the result of above print)
            file = open('testfile.csv', 'ab')
            file.write(serBytes)
            file.close()

            # check if <esc> was pressed; stop if so
        #if kb.is_pressed('esc'):
         #   break;

    # close serial port
    ser.close
except:
    print("Unexpected error:", sys.exc_info()[0])
    print("Unexpected error:", sys.exc_info()[1])

    # maybe todo: close serial port; this might need a little rework of above code moving 'ser = serial.Serial('COM4', baudrate=57600)' to outside the try
