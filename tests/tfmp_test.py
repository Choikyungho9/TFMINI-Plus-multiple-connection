'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
* File Name: TFMP_example.py
* Inception: 14 MAR 2021
* Developer: Bud Ryerson
# Version:   0.0.1
* Last work: 30 MAR 2021

* Description: Python script to test the Benewake TFMini Plus
* time-of-flight Lidar ranging sensor in Serial (UART) mode
* using the 'TFMPlus.py' module in development.

* Default settings for the TFMini-Plus are a 115200 serial baud rate
* and a 100Hz measurement frame rate. The device will begin returning
* three measurement datums right away:
*   Distance in centimeters,
*   Signal strength in arbitrary units and
*   Temperature encoded for degrees centigrade

* Use the 'sendCommand()' to send a command and a parameter.
* Returns a boolean result and sets a one byte status code.
* Commands are defined in the module's list of commands.
* Parameters can be entered directly (115200, 250, etc) but for
* safety, they should be chosen from the module's defined lists.

* NOTE:
*   GPIO15 (RPi Rx pin) connects to the TFMPlus Tx pin and
*   GPIO14 (RPi Tx pin) connects to the TFMPlus Rx pin
*

* Press Ctrl-C to break the loop
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
import time
import sys
from datetime import datetime
import tfmplus1 as tfmP   # Import the `tfmplus` module v0.0.2
import tfmplus2 as tfmP2
import tfmplus3 as tfmP3
import tfmplus4 as tfmP4
import tfmplus5 as tfmP5
from tfmplus1 import *    # and also import all its defintions

serialPort1 = "/dev/ttyAMA0"  # Raspberry Pi normal serial port
serialPort2 = "/dev/ttyAMA1"
serialPort3 = "/dev/ttyAMA2"
serialPort4 = "/dev/ttyAMA3"
serialPort5 = "/dev/ttyAMA4"

serialRate = 115200          # TFMini-Plus default baud rate

# - - - Set and Test serial communication - - - -
print( "Serial port: \n", end= '')
if(tfmP.begin(serialPort1, serialRate)):
    print( "lidar1 is ready")
    #time.sleep(0.5)
if(tfmP2.begin(serialPort2, serialRate)):
    print( "lidar2 is ready")
    #time.sleep(0.5)
if(tfmP3.begin(serialPort3, serialRate)):
    print( "lidar3 is ready")
    #time.sleep(0.5)
if(tfmP4.begin(serialPort4, serialRate)):
    print( "lidar4 is ready")
    #time.sleep(0.5)
if(tfmP5.begin(serialPort5, serialRate)):
    print( "lidar5 is ready")
    #time.sleep(0.5)
else:
    print( "not ready")
    sys.exit()   #  quit the program if serial not ready

# - - Perform a system reset - - - - - - - -
#print( "System reset: ", end= '')
#if( tfmP1.sendCommand( SYSTEM_RESET, 0)):
#    print( "passed.")
#else:
#    tfmP1.printReply()
#time.sleep(0.5)  # allow 500ms for reset to complete

# - - Display the firmware version - - - - - - - - -
#print( "Firmware version: ", end= '')
#if( tfmP1.sendCommand( OBTAIN_FIRMWARE_VERSION, 0)):
#    print( str( tfmP1.version[ 0]) + '.', end= '') # print three numbers
#    print( str( tfmP1.version[ 1]) + '.', end= '') # separated by a dot
#    print( str( tfmP1.version[ 2]))
#else:
#    tfmP1.printReply()

# - - Set the data frame-rate to 20Hz - - - - - - - -
print( "Data-Frame rate: \n", end= '')
if( tfmP.sendCommand( SET_FRAME_RATE, FRAME_100)):
    print('lidar1 FRAME_RATE:', str(FRAME_100) + 'Hz')
if( tfmP2.sendCommand( SET_FRAME_RATE, FRAME_100)):
    print('lidar2 FRAME_RATE:', str(FRAME_100) + 'Hz')
if( tfmP3.sendCommand( SET_FRAME_RATE, FRAME_100)):
    print('lidar3 FRAME_RATE:', str(FRAME_10) + 'Hz')
if( tfmP4.sendCommand( SET_FRAME_RATE, FRAME_100)):
    print('lidar4 FRAME_RATE:', str(FRAME_100) + 'Hz')
if( tfmP5.sendCommand( SET_FRAME_RATE, FRAME_100)):
    print('lidar5 FRAME_RATE:', str(FRAME_100) + 'Hz')
#    time.sleep(0.1)
else:
    tfmP3.printReply()

# - - - - - - - - - - - - - - - - - - - - - - - -
time.sleep(0.5)            # And wait for half a second.

# - - - - - -  the main program loop begins here  - - - - - - -
try:
    while True:
        time.sleep(0.001)   # Loop delay 50ms to match the 20Hz data frame rate
        # Use the 'getData' function to get data from device
        if(tfmP.getData()&tfmP2.getData()&tfmP3.getData()&tfmP4.getData()&tfmP5.getData()):
            #print( f"\n Dist_lidar1: {tfmP.dist:{3}}cm ", end= '' )   # display distance,
                #if(tfmP2.getData()):
            #print( f"\n Dist_lidar2: {tfmP2.dist:{3}}cm \n", end= '')   # display distance,
                    #if(tfmP3.getData()):
            #print( f"\n Dist_lidar3: {tfmP3.dist:{3}}cm \n", end= '')   # display distance,
                        #if(tfmP4.getData()):
            #print( f"\n Dist_lidar4: {tfmP4.dist:{3}}cm \n", end= '')   # display distance,
                            #if(tfmP5.getData()):
            #print( f"\n Dist_lidar5: {tfmP5.dist:{3}}cm \n", end= '')   # display distance,   
            print(datetime.utcnow().strftime('%H:%M:%S.%f')[:-3], tfmP.dist, tfmP2.dist, tfmP3.dist, tfmP4.dist, tfmP5.dist)
        else:                  # If the command fails...
            tfmP1.printFrame()    # display the error and HEX data
            tfmP2.printFrame()
            tfmP3.printFrame()
            tfmP4.printFrame()
            tfmP5.printFrame()
except KeyboardInterrupt:
    print( 'Keyboard Interrupt')
#    
except: # catch all other exceptions
    eType = sys.exc_info()[0]  # return exception type
    print( eType)
#
finally:
    print( "exit")
    sys.exit()                   # clean up the OS and exit
#
# - - - - - -  the main program sequence ends here  - - - - - - -
