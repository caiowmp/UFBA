from socket import *
import os
import struct
import time
import sys

def connectToHub():
	HubName = 'localhost'
	HubPort = 12001

	try:
		clientSocket = socket(AF_INET, SOCK_STREAM)
		print('Initiating TCP connection with server', HubName, 'over port', HubPort, '...')
		clientSocket.connect((HubName,HubPort))
	except:
		print('Could not make a connection to the server')
		print('Try again')
		return False


	clientSocket.send(struct.pack('i', int(serverPort)))

	print('Waiting server response...')
	response = clientSocket.recv(1024).decode()

	print('From Hub:', response)

	print('Closing TCP connection...')
	clientSocket.close()
	print('Finish.')
	if response == 'OK':
		connectedToHub = True

	return connectedToHub

def deposit(connectionSocket):
	size_filename = struct.unpack('i',connectionSocket.recv(4))[0]
	filename = connectionSocket.recv(size_filename).decode()
	print('Filename:', filename)

	file = open('server_folders/'+serverPort+'/'+filename,'wb')
	
	print('Receiving file...')
	packet = connectionSocket.recv(1024)
	while (packet):
		file.write(packet)
		packet = connectionSocket.recv(1024)

	file.close()
	print('File received. Notifying Hub...')
	response = 'OK'
	connectionSocket.send(response.encode())

def recovery(connectionSocket):
	size_filename = struct.unpack('i',connectionSocket.recv(4))[0]
	filename = connectionSocket.recv(size_filename).decode()
	print('Filename:', filename)
	
	try:
		file = open('server_folders/'+serverPort+'/'+filename,'rb')
		print('File available. Notifying Hub...')
		response = 'ACK'
		connectionSocket.send(response.encode())
	except:
		print('No such file or directory named:', filename)
		response = 'NCK'
		print('Notifying Hub...')
		connectionSocket.send(response.encode())

	request = connectionSocket.recv(3).decode()
	if request == 'ACK':
		print("Sending file to Hub...")
		packet = file.read(1024)
		while (packet):
			connectionSocket.send(packet)
			packet = file.read(1024)
		file.close()
		print('File sent. Notifying Hub...')
		connectionSocket.shutdown(SHUT_WR)

def remove(connectionSocket):
	size_filename = struct.unpack('i',connectionSocket.recv(4))[0]
	filename = connectionSocket.recv(size_filename).decode()
	print('Filename:', filename)

	if os.path.exists('server_folders/'+serverPort+'/'+filename):
		print("File exist. Removing file...")
		os.remove('server_folders/'+serverPort+'/'+filename)
		response = 'ACK'
	else:
		print("The file does not exist")
		response = 'NCK'

	print("Notifying Hub")
	connectionSocket.send(response.encode())

serverPort = input('Insert Server Port: ') 
directory_path = os.getcwd()
new_abs_path = os.path.join(directory_path, 'server_folders')
new_abs_path = os.path.join(new_abs_path, serverPort)
if not os.path.exists(new_abs_path):
	os.mkdir(new_abs_path)

t1 = time.time()
connectedToHub = False
while time.time()-t1 < 2 and not connectedToHub:
	connectedToHub = connectToHub()

if not connectedToHub:
	print("Server didn't connect to Hub.")
	sys.exit(0)

# Now let's start server
serverPortInt = int(serverPort)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPortInt))
serverSocket.listen(1)
print()
print('The server is ready to receive')


while 1:
	connectionSocket, addr = serverSocket.accept()
	try:
		operation = struct.unpack('i',connectionSocket.recv(4))[0]
		if operation == 1:
			print('Deposit operation.')
			deposit(connectionSocket)
		elif operation == 2:
			print('Recovery operation.')
			recovery(connectionSocket)
		elif operation == 3:
			print('Remove operation.')
			remove(connectionSocket)

		print()

		print("Closing connection with Hub.")
		print()
		connectionSocket.close()
	except Exception as e:
		print('An error ocurred:', e)
		print("Closing connection with Hub.")
		print()
		connectionSocket.close()