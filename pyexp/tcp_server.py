"""
tcp_server.py
"""
import socket
import json    # for serialize data

s = socket.socket()
host = socket.gethostname()
port = 12345   # maximum is 65536, which is max of 16 bits
s.bind((host, port))
print("Start listening.")
print(s)
s.listen(5)
while True:
    c, address = s.accept()
    print("Got connection from :", address)
    message = "Thank you for connecting"
    c.send(json.dumps(message).encode("utf-8"))
    lst = json.loads(c.recv(1024).decode("utf-8"))
    print("Sum of the list: " + str(sum(lst)))
    # sustain the chat program
    while True:
        custom_msg = json.loads(c.recv(1024).decode("utf-8"))
        if custom_msg == "q":
            print("Oh no the client leave me!")
            break
        print(custom_msg)
    c.close()
