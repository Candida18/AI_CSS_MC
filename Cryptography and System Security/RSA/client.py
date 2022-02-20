# Import socket module
import socket

import math

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(("127.0.0.1", port))

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())


n, e = [int(i) for i in s.recv(2048).decode("utf-8").split("\n")]
print("e from server {} , n from server {}".format(e, n))
msg = int(input("Enter the plaintext (M) : "))

print("The Public Key - PU = ({},{})".format(e,n))
cipher_text = pow(msg, e) % n
print("Cipher Text : ", cipher_text)
s.send(str(cipher_text).encode())

# close the connection
s.close()
