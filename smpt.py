#!/bin/bash/python
import socket
import sys


if len(sys.argv) !=3:
    print("how to use: ./smpt.py ip user")
    exit(0)

print("startig ...")
ip=sys.argv[1]
user=sys.argv[2]
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c=s.connect((ip,25))
data=s.recv(1024)
print(data)
s.send(f"VRFY"+user+"/r/n".encode())
data2=s.recv(1024).decode()
print(data2)
s.close()