import serial, traceback
from driver import *

class DiamexLedPlayer(Driver):
    """Driver for DiamexLedPlayer"""
    
    def __init__(self, dev="/dev/tty.usbmodem1411"):
        super(DiamexLedPlayer, self).__init__(dev)

        self.ser = serial.Serial()
        self.ser.port = dev
        self.ser.writeTimeout = 2
    
        try:
            self.ser.open()

        except Exception, e:
            print "Error while opening serial port: " + str(e)
            print traceback.format_exc()
            exit()
                

    def __del__(self):
        if self.ser.isOpen():
            self.ser.close()


    def getNumBytes(self, numLeds):
    
        numBytes = numLeds * 3
    
        result = bytearray(2)
        result[0] = (numBytes >> 8) & 0xFF
        result[1] = numBytes & 0xFF
    
        return result


    def update(self, buffer):
    
        if self.ser.isOpen():
        
            try:
                self.ser.flushInput()
                self.ser.flushOutput()
            
                numLeds = len(buffer)
                
                output = b"\xC9\xDA"
                output += self.getNumBytes(numLeds)

                for x in range(numLeds):
                    output += buffer[x]
                
                output += b"\x36"
                
                self.ser.write(output)

            except Exception, e:
                print "Error while trying to send serial data: " + str(e)
                print traceback.format_exc()
    
        else:
            print "Error: Serial port is not open"


    

