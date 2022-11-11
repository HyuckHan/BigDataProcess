from socket import *

BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 8080))

print("Input \"exit\" to quit")

while 1:
    msg = input("> ")
    s.send(msg.encode("UTF-8"))
    if msg == "exit": break;
    rtn = s.recv(BUFSIZE).decode("UTF-8")
    print(rtn)

s.close()
