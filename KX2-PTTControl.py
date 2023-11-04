####################################################################################
# KX2 Transceiver PTT control via PC keybaord
#
# This python script waits for pressing a certain key and then sends commands to the 
# Elecraft KX2 transceiver.
#
# Currently you can control the PTT key by pressing the right "Strg" key on the
# keyboard and you can play the content of the two voide memories; voice memory 1 by pressing the 
# "Start Browser" key and the "Start Calculator" key for voice memory 2.
# I am using this memory e.g. to send my call sign (in German and in English).
#
# Creator:  Michael Urspringer (DG3NAB)
# Version:  1.1
####################################################################################

# Import the necessary Python modules
import keyboard
import serial
import os

# Define keyboard control keys
PTT_Event   = "strg-rechts"              # Key for PTT on/off switch
MEM1_Event  = "browser start and home"   # Key "Start Browser" for replay of voice memeory 1
MEM2_Event  = "start application 2"      # Key "Start Calculator" for replay of voice memeory 2


# Open the serial COM port which is connected to the transceiver
serialPort = serial.Serial(
    port="COM19", baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, xonxoff=False, rtscts=False, dsrdtr=False, timeout=2
)

# Initialize PTT status (set to OFF)
serialPort.write(b'RX;')  
pttStatus = "OFF"

# Clearing the Screen and print status message
os.system('cls')
print("Elecraft KX2-PTTControl running in background")
print ("Press Strg/Ctrl-C to stop.")
print (" ")
print ("Right Strg/Ctrl key:    Toggle PTT")
print ("Browser key:            Play Voice Memory 1")
print ("Calculator key:         Play Voice Memory 2")

try:

    # Do this forever (until the program is terminated via Strg-C
    while True:

        # Wait for the next keyboard event
        event = keyboard.read_event()

        print(event.name)  # Uncomment this to see how whet the exact name of the keyboard even is
        
        if event.event_type == keyboard.KEY_DOWN and event.name == PTT_Event:
            # The key for the PTT on/off has been pressed
            if pttStatus == "OFF":
                # Current PTT status is off, so switch PTT on
                serialPort.write(b'TX;')
                pttStatus = "ON"
            else:
                # Current PTT status is on, so switch PTT off
                serialPort.write(b'RX;')
                pttStatus = "OFF"
        elif event.event_type == keyboard.KEY_DOWN and event.name == MEM1_Event:
            # The key for playing the voice memory 1 has been pressed, so play voice memory 1
            serialPort.write(b'SWT11;SWT19;')
        elif event.event_type == keyboard.KEY_DOWN and event.name == MEM2_Event:
            # The key for playing the voice memory 2 has been pressed, so play voice memory 2
            serialPort.write(b'SWT11;SWT27;')

except:
    print (" ")
    print("KX2-PTTControl ended.")