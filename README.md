# KX2 Transceiver PTT control via PC keybaord

This python script waits for pressing a certain key and then sends commands to the 
Elecraft KX2 transceiver.

Currently you can control the PTT key by pressing the right "Strg"/"Ctrl" key on the
keyboard and you can play the content of the voice memory 2 by pressing the 
"AltGr" key. I am using this memory e.g. to send my call sign.

The script will be called by:

`python <PathToFile>\KX2-PTTControl.py`

It is running in the background until you stop it by pressing "Strg-C".

You can also create a one file executable by uusing "pyinstaller" (https://pyinstaller.org/en/stable/) like that:

`pyinstaller --onefile ..\KX2-PTTControl.py`