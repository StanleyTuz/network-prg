import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    mySocket = socket.socket()
    mySocket.connect((host,port))

    message = input(" -> ")

    while message != 'q':
        mySocket.send(message.encode())
        # client does not need to bind
        
        data = mySocket.recv(1024).decode() # receive a response

        print("Received from server: " + data)

        message = input(" -> ")

    mySocket.close()

if __name__ == "__main__":
    Main()