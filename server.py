import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

# Function to handle incoming HTTP requests
def handle_request(clientsocket, address):
    print('conn')
    request = clientsocket.recv(1024).decode('utf-8')
    print(request)
    response = ''
    if request[0:3] == "GET":
        filename = request.split(' ')[1]
        print(f'filething: {filename}')
        response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        try:
            with open(filename[1:], 'rb') as file:
                response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                content = file.read()
                response += content
        except:
            print('oh no ')
            response = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
            response += b'404 - Page Not Found'
        
    
    c.sendall(response)
    c.close()

# Create a TCP socket
server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Serving at port {PORT}")

while True:
    # Accept a new connection
    c, addr = server_socket.accept()

    t = threading.Thread(target=handle_request, args=(c, addr,))
    t.start()

    