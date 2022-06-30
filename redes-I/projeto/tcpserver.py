from socket import *
import os
import struct
import time
import sys

serverPort = input('Insert Server Port: ') 
directory_path = os.getcwd()
new_abs_path = os.path.join(directory_path, 'server_folders')
new_abs_path = os.path.join(new_abs_path, serverPort)
if not os.path.exists(new_abs_path):
	os.mkdir(new_abs_path)

t1 = time.time()
connectedToHub = False
while time.time()-t1 < 2:
	hubName = 'localhost'
	hubPort = 12001

	try:
		clientSocket = socket(AF_INET, SOCK_STREAM)
		print('Initiating TCP connection with server', hubName, 'over port', hubPort, '...')
		clientSocket.connect((hubName,hubPort))
	except:
		print('Could not make a connection to the server')
		print('Try again')
		continue


	clientSocket.send(struct.pack('i', int(serverPort)))

	print('Waiting server response...')
	response = clientSocket.recv(1024).decode()

	print('From Hub:', response)

	print('Closing TCP connection...')
	clientSocket.close()
	print('Finish.')
	if response == 'OK':
		connectedToHub = True
	break

if not connectedToHub:
	print("Server didn't connect to Hub.")
	sys.exit(0)

# Now let's start server
serverPortInt = int(serverPort)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPortInt))
serverSocket.listen(1)
print('The server is ready to receive')


while 1:
	connectionSocket, addr = serverSocket.accept()
	operation = struct.unpack('i',connectionSocket.recv(4))[0]
	if operation == 1:
		size_filename = struct.unpack('i',connectionSocket.recv(4))[0]
		print(size_filename)
		packet = connectionSocket.recv(size_filename)
		print(packet)
		filename = packet.decode()
		# filename = connectionSocket.recv(1024).decode()
		print(filename)
		file = open('server_folders/'+serverPort+'/'+filename,'wb')
		
		packet = connectionSocket.recv(1024)
		while (packet):
			file.write(packet)
			packet = connectionSocket.recv(1024)

		file.close()
		ack = 'OK'
		connectionSocket.send(ack.encode())
	elif operation == 2:
		size_filename = struct.unpack('i',connectionSocket.recv(4))[0]
		print(size_filename)
		packet = connectionSocket.recv(size_filename)
		filename = packet.decode()
		print(filename)
		try:
			file = open('server_folders/'+serverPort+'/'+filename,'rb')
			response = 'ACK'
			connectionSocket.send(response.encode())
		except:
			print('No such file or directory named: ', filename)
			response = 'NCK'
			connectionSocket.send(response.encode())

		request = connectionSocket.recv(3).decode()
		if request == 'ACK':
			print("Sending file to HUB...")
			packet = file.read(1024)
			while (packet):
				connectionSocket.send(packet)
				packet = file.read(1024)
			file.close()
			print('File downloaded. Notifying hub...')
			connectionSocket.shutdown(SHUT_WR)

	elif operation == 3:
		size_filename = struct.unpack('i',connectionSocket.recv(4))[0]
		print(size_filename)
		packet = connectionSocket.recv(size_filename)
		filename = packet.decode()
		print(filename)

		if os.path.exists('server_folders/'+serverPort+'/'+filename):
			os.remove('server_folders/'+serverPort+'/'+filename)
			response = 'ACK'
		else:
			print("The file does not exist")
			response = 'NCK'

		connectionSocket.send(response.encode())

	print("Closing connection with HUB.")
	connectionSocket.close()
