from socket import *
from threading import Thread
import time
import sys
import struct

class ListenServers(Thread):

	def __init__(self, num):
		Thread.__init__(self)
		self.num = num
		self.portsAvailable = []

	def run(self):
		serverPort = 12001
		hubSocket = socket(AF_INET,SOCK_STREAM)
		hubSocket.bind(('',serverPort))
		hubSocket.listen(1)
		print('The Hub is ready to receive from Servers')


		while 1:
			connectionSocket, addr = hubSocket.accept()
			print('Connected to server', addr)
			port = struct.unpack('i',connectionSocket.recv(4))[0]
			print('Port received', port)
			if port not in self.portsAvailable:
				self.portsAvailable.append(port)
				response = 'OK'
			else:
				print("Port", port,"is already available")
				response = "Port is already available"

			print(self.portsAvailable)
			connectionSocket.send(response.encode())
			connectionSocket.close()


class ListenClient(Thread):

	def __init__(self, num, threadServers):
		Thread.__init__(self)
		self.num = num
		self.threadServers = threadServers

	def run(self):
		serverPort = 12000
		hubSocket = socket(AF_INET,SOCK_STREAM)
		hubSocket.bind(('',serverPort))
		hubSocket.listen(1)
		print('The Hub is ready to receive from Client')


		while 1:
			clientConnectionSocket, clientAddr = hubSocket.accept()
			operation = struct.unpack('i',clientConnectionSocket.recv(4))[0]

			if operation == 1:
				size_filename = struct.unpack('i',clientConnectionSocket.recv(4))[0]
				print(size_filename)
				filename = clientConnectionSocket.recv(size_filename).decode()
				ft_level = struct.unpack('i',clientConnectionSocket.recv(4))[0]
				file = open('temp','wb')
				
				packet = clientConnectionSocket.recv(1024)
				while (packet):
					file.write(packet)
					packet = clientConnectionSocket.recv(1024)

				file.close()

				for serverPort in self.threadServers.portsAvailable:
					serverName = 'localhost'

					try:
						clientHubSocket = socket(AF_INET, SOCK_STREAM)
						print('Initiating TCP connection with server', serverName, 'over port', serverPort, '...')
						clientHubSocket.connect((serverName,serverPort))
					except:
						print('Could not make a connection to the server', serverPort)
						continue

					try:
						file = open('temp','rb')
					except:
						print('No such file or directory named: ', filename)
						sys.exit(0)

					print("Sending operation.")
					clientHubSocket.send(struct.pack('i', 1))
					print('Sending filename')
					print(filename)
					clientHubSocket.send(struct.pack('i',size_filename))
					clientHubSocket.send(filename.encode())
					print('Sending file to server', serverName, 'over port', serverPort, '...')
					packet = file.read(1024)
					while (packet):
						clientHubSocket.send(packet)
						packet = file.read(1024)

					file.close()
					print('File uploaded. Notifying server...')
					clientHubSocket.shutdown(SHUT_WR)

					print('Waiting server response...')
					response = clientHubSocket.recv(1024)

					print('From Server:', response.decode())

					print('Closing TCP connection...')
					clientHubSocket.close()
					print('Finish.')
					ft_level -= 1
					if ft_level == 0:
						break

				if ft_level == 0:
					response = 'OK'
				else:
					response = 'Tolerance Level not accomplished: '+str(ft_level)
				
				clientConnectionSocket.send(response.encode())
			elif operation == 2:
				size_filename = struct.unpack('i',clientConnectionSocket.recv(4))[0]
				print(size_filename)
				filename = clientConnectionSocket.recv(size_filename).decode()

				file_available = False
				for serverPort in self.threadServers.portsAvailable:
					serverName = 'localhost'

					try:
						clientHubSocket = socket(AF_INET, SOCK_STREAM)
						print('Initiating TCP connection with server', serverName, 'over port', serverPort, '...')
						clientHubSocket.connect((serverName,serverPort))
					except:
						print('Could not make a connection to the server', serverPort)
						continue

					print("Sending operation.")
					clientHubSocket.send(struct.pack('i', 2))

					print('Sending filename')
					print(filename)
					clientHubSocket.send(struct.pack('i',size_filename))
					clientHubSocket.send(filename.encode())

					print('Waiting server response...')
					response = clientHubSocket.recv(3).decode()
					print(response)
					if response == 'ACK':
						print("Server", serverName, "in port", serverPort, "has the file", filename, ".")
						file_available = True
						try:
							file = open('temp','wb')
						except:
							print("Not possible to create the file")
							sys.exit(0)


						packet = clientHubSocket.recv(1024)
						while (packet):
							file.write(packet)
							packet = clientHubSocket.recv(1024)
						file.close()
					else:
						print("Server", serverName, "in port", serverPort, "doesn't have the file", filename, ".")

					print('Closing TCP connection...')
					clientHubSocket.close()
					print('Finish.')

					if response == 'ACK':
						break

				if file_available:
					response = 'ACK'
					clientConnectionSocket.send(response.encode())
					try:
						file = open('temp','rb')
					except:
						print('No such file or directory named: ', filename)
						sys.exit(0)

					print("Sending file to client...")
					packet = file.read(1024)
					while (packet):
						clientConnectionSocket.send(packet)
						packet = file.read(1024)

					file.close()
					print('File downloaded. Notifying client...')
					clientConnectionSocket.shutdown(SHUT_WR)
				else:
					response = 'NCK'
					clientConnectionSocket.send(response.encode())

			clientConnectionSocket.close()


threadServers = ListenServers(1)
threadServers.start()

threadClient = ListenClient(1, threadServers)
threadClient.start()		
