####################################################################################
# KX2 Transceiver PTT control via PC keybaord
#
# This python script waits for pressing a certain key and then sends commands to the 
# Elecraft KX2 transceiver.
#
# Currently you can control the PTT key by pressing the right "Strg" key on the
# keyboard and you can play the content of the voice memory 2 by pressing the 
# "AltGr" key. I am using this memory e.g. to send my call sign.
#
# Creator:  Michael Urspringer (DG3NAB)
# Version:  1.0
####################################################################################

# Import the necessary Python modules
import keyboard
import serial

# Define keyboard control keys
PTT_Event = "strg-rechts"   # Key for PTT on/off switch
MEM2_Event = "alt gr"       # Key for replay of voice memeory 2

# Open the serial COM port which is connected to the transceiver
serialPort = serial.Serial(
    port="COM19", baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, xonxoff=False, rtscts=False, dsrdtr=False, timeout=2
)

# Initialize PTT status (set to OFF)
serialPort.write(b'RX;')  
pttStatus = "OFF"

# Do this forever (until the program is terminated via Strg-C
while True:

    # Wait for the next keyboard event
    event = keyboard.read_event()

    # print(event.name)  # Uncomment this to see how whet the exact name of the keyboard even is
    
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
    elif event.event_type == keyboard.KEY_DOWN and event.name == MEM2_Event:
        # The key for playing the voice memory 2 has been pressed, so play voice memory
        serialPort.write(b'SWT11;SWT27;')
        