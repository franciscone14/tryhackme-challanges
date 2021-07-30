#!/usr/bin/python3
import socket, sys

IP = "127.0.0.1"
PORT = 9999

def printRecv(s: socket):
    data = s.recv(1024)
    print(data.decode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)
    s.connect((IP, PORT))
    printRecv(s)
    s.send("whistleblower".encode('utf-8'))
    printRecv(s)
    payload = 'A' * 100
    while True:
        try:
            print("Fuzzing with {} bytes".format(len(payload)))
            s.send(bytes(payload, "latin-1"))
            printRecv(s)
        except:
            print("Server Crashed")
            sys.exit(0)
        payload += 100 * 'A'