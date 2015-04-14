#!/usr/bin/env python
#
# GrovePi Example for using the Grove Dust sensor
# (http://www.seeedstudio.com/wiki/Grove_-_Dust_Sensor)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# LICENSE: 
# These files have been made available online through a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/) license.

import time
import grovepi

# Connect the Grove Dust Sensor to digital port D3
# SIG,NC,VCC,GND
#dustPin = 3

period = 60

if __name__ == '__main__':
    #grovepi.dustSensor_init()

    while True:
        if time.time() > (lastUp+period): 
            try:
                print("Concentration: %s" % grovepi.readDustSensor())
            except TypeError:
                print("Error")
            except IOError:
                print("Error")
            lastUp = time.time()
