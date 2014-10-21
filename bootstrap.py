#!/usr/bin/python

"""
use "from bootstrap import *" from any script to do all the standard setup 
and checks needed by any script
"""

from time import sleep
from raspledstrip.ledstrip import *
from raspledstrip.animation import *

import os.path
import sys

# Check that the system is set up like we want it
dev = '/dev/tty.usbmodem1411'

if not os.path.exists(dev):
    sys.stderr.write("""
The selected device does not exist. You may need to load
the appropriate kernel modules. 

For using SPI try:

sudo modprobe spi_bcm2708 ; sudo modprobe spidev

You may also need to unblacklist the spi_bcm2708 module in 
/etc/modprobe.d/raspi-blacklist.conf

""")
    sys.exit(2)

#permissions check
#try:
#    open(dev)
#except IOError as  e:
#   if e.errno == 13:
#        sys.stderr.write("""
#It looks like SPI device /dev/spidev0.0 has the wrong permissions.
#Try making it world writable:
#
#sudo chmod a+rw /dev/spidev0.0
#
#""")
#    sys.exit(2)

num = 240
led = LEDStrip(num, driver="Diamex", dev="/dev/tty.usbmodem1411")#led.setChannelOrder(ChannelOrder.BRG) #Only use this if your strip does not use the GRB order
#led.setMasterBrightness(0.5) #use this to set the overall max brightness of the strip
led.all_off()