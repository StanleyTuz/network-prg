import socket

def Main():
    # local machine is host with ip addr 127...
    # randomly use port 5000 > 1024 (core services use below 1024)
    host = "127.0.0.1"
    port = 5000

    # define socket variable
    mySocket = socket.socket()
    # bind socket to host and port 
    mySocket.bind((host,port))

    # wait and listen (pass 1 to perpetually listen til closed)
    mySocket.listen(1)
    # hold connection from client, addr of client
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode() # var to receieve the data, decode it
        if not data:
            break
        print("from connected user: " + str(data))

        data = str(data).upper()
        print("sending: " + str(data))
        conn.send(data.encode())

    conn.close()

if __name__ == "__main__":
    Main()

