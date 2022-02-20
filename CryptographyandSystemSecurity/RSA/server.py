# first of all import the socket library
import socket
import math

# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(("", port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("Socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    c, addr = s.accept()
    print("Got connection from", addr)

    # send a thank you message to the client. encoding to send byte type.
    c.send("Connection established".encode())

    p = int(input("Enter the value of p: "))
    q = int(input("Enter the value of q: "))

    n = p * q

    tfun = (p - 1) * (q - 1)

    for e in range(2, tfun):
        if math.gcd(e, tfun) == 1:
            break

    for i in range(1, 50):
        x = 1 + i * tfun
        if x % e == 0:
            d = int(x / e)
            break

    # print(d)
    c.sendall(str.encode("\n".join([str(n), str(e)])))

    print("The Private Key - PR = ({},{})".format(d,n))

    cipher = int(c.recv(1024).decode())

    plain_text = pow(cipher, d) % n
    print("Plain Text (after decryption): ",plain_text)

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break
