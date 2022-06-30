from socket import *
import os
import sys
import struct

def deposit():
	clientSocket.send(struct.pack('i', 1))

	filepath = input('Input filename: ')
	filename = os.path.basename(filepath)
	size_filename = len(filename)
	print(size_filename)
	clientSocket.send(struct.pack('i',size_filename))
	clientSocket.send(filename.encode())
	print('Filename sent')

	ft_level = int(input('Input fault tolerance level: '))
	print('Sending Fault Tolerance Level')
	clientSocket.send(struct.pack('i',ft_level))
	print('Fault Tolerance Level sent')

	request = clientSocket.recv(3).decode()
	if request == 'ACK':		
		try:
			file = open(filepath,'rb')
		except:
			print('No such file or directory named: ', filepath)
			sys.exit(0)

		print('Sending file to server', serverName, 'over port', serverPort, '...')
		packet = file.read(1024)
		while (packet):
			clientSocket.send(packet)
			packet = file.read(1024)

		file.close()
		print('File uploaded. Notifying server...')
		clientSocket.shutdown(SHUT_WR)

	print('Waiting server response...')
	response = clientSocket.recv(1024)

	print('From Server:', response.decode())

def recovery():
	clientSocket.send(struct.pack('i', 2))

	filename = input('Input filename: ')
	size_filename = len(filename)
	print(size_filename)
	clientSocket.send(struct.pack('i',size_filename))
	clientSocket.send(filename.encode())
	print('Filename sent')

	print('Waiting server response...')
	response = clientSocket.recv(3).decode()
	print(response)
	if response == 'ACK':	
		try:
			file = open("local_folders/"+filename,'wb')
		except:
			print("Not possible to create the file")
			sys.exit(0)

		packet = clientSocket.recv(1024)
		while (packet):
			file.write(packet)
			packet = clientSocket.recv(1024)

		file.close()
		print("File recovered succesfully.")
	else:
		print("File not available.")


serverName = 'localhost'
serverPort = 12000

try:
	clientSocket = socket(AF_INET, SOCK_STREAM)
	print('Initiating TCP connection with server', serverName, 'over port', serverPort, '...')
	clientSocket.connect((serverName,serverPort))
except:
	print('Could not make a connection to the server')
	print('Try again')
	sys.exit(0)

print("List of operations available:")
print("[1] Deposit Mode")
print("[2] Recovery Mode")
operation = input("Input the number of the operation you want to do: ")

while operation != '1' and operation != '2':
	print("List of operations available:")
	print("[1] Deposit Mode")
	print("[2] Recovery Mode")
	operation = input("Input the number of the operation you want to do: ")

if operation == '1':
	deposit()
elif operation == '2':
	recovery()

print('Closing TCP connection...')
clientSocket.close()
print('Finish.')
