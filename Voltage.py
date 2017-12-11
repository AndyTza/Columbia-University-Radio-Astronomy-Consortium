#!/usr/bin/python

"""
Listen to serial, return most recent numeric values --- returns voltage values numerically 
"""

import time
import serial
import datetime
import random



class SerialData(object):
    def __init__(self, init=50):
        try:
            self.ser = ser = serial.Serial(
                port='/dev/cu.usbmodem1411',
                baudrate=9600,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=0.1,
                xonxoff=0,
                rtscts=0,
                interCharTimeout=None
            )
        except serial.serialutil.SerialException:
            #no serial connection
            self.ser = None
  
    def next(self):
        if not self.ser:
            print "here!"
            return 0 #100
        while True:                                        # 
            if (self.ser.inWaiting()>0):
                myData = float(self.ser.readline().strip())
                                                                                     #	print myData
                                                                                         #	        timestamp = datetime.datetime.now()
            if(myData<1.2):                                                                # and not ValueError):                                             #Filtering the values
                return myData
                                                                                         #	            print >>f, timestamp,"\t",int(time.time()),"\t",myData
                                                                                         #		    return random.randrange(15)


    def __del__(self):
        if self.ser:
            self.ser.close()
#            f.close()

if __name__=='__main__':
    s = SerialData()
    for i in range(500):
        time.sleep(.015)
        print s.next()
