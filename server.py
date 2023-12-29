import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a new sucket subject for the server AF_inet (IPv4)
server.bind(("localhost", 8888)) # Binds the server into the existing port

server.listen() #Puts the server into a listning state

client, addr = server.accept()

done = False

while not done:
    msg = client.recv(1024).decode('utf-8') # recieves data(up to 1024bytes)
    if msg == 'quit':
        done = True
    else:
        print(msg)
    client.send(input("Mesage: ").encode('utf-8')) # Propt the user to input a message


client.close()
server.close()