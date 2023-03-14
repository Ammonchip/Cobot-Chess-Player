import socket
import time

HOST = "10.224.1.115"
PORT = 30002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
time.sleep(1)
f = open("myFun.script", "rb")
l = f.read(1024)
print(l)

#f = open("URCap_Release.script", "rb")
#release = f.read()

s.send(("movel(p[-0.487, 0.308, 0.102, 3, -1.2, 0], a=1.2, v=0.25, t=0, r=0)"+"\n").encode('utf8'))

#s.send(grip)
time.sleep(5)
data = s.recv(1024)
s.close()
print ("Received", repr(data))