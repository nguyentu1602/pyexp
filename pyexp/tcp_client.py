"""
tcp_client.py
"""
import socket
import json
client_s = socket.socket()
host = socket.gethostname()
port = 12345
print("about to connect")
client_s.connect((host, port))
message = json.loads(client_s.recv(1024).decode("utf-8"))
print(message)
lst = [1, 4, 4]
client_s.send(json.dumps(lst).encode("utf-8"))
# chat program:
while True:
    custom_msg = input("-> ")
    custom_msg = str(custom_msg)
    client_s.send(json.dumps(custom_msg).encode("utf-8"))
    if custom_msg == "q":
        client_s.close()
        break
