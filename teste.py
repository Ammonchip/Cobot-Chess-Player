import socket
import time


HOST = "10.224.1.115"
PORT = 30002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
f = open("URCap_Grip.script", "rb")
grip = f.read()
f = open("URCap_Release.script", "rb")
release = f.read()
count = 0
while(count < 1):
    s.send(release)
    time.sleep(10)
    count += 1