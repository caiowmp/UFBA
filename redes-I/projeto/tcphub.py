"""
Hub da aplicação

Escuta os servidores e os clients que conectam com ele mesmo e executa as operações enviadas pelo client nos servers.
"""

from socket import *
from threading import Thread
import time
import sys
import struct
import os

class ListenServers(Thread):
	"""
	Thread que escuta os servidores que estão conectando com o hub.

	...

	Attributes
	----------
	num : int
		Numero da thread
	portsAvailable : list of int
		Portas dos servidores conectados com o hub

	"""

	def __init__(self, num):
		"""
		Constroi todos os atributos e inicia o thread

		Parameters
		----------
		num : int
			Numero da thread
		"""
		Thread.__init__(self)
		self.num = num
		self.portsAvailable = []

	def contactServer(self, serverPort):
		"""
		Contacta o servidor e verifica se a conexão com o mesmo ainda é possível

		Parameters
		----------
		serverPort : int
			Porta do servidor que será contatado

		Returns
		-------
		bool
			Estado da conexão com o servidor contatado
		"""
		serverName = 'localhost'
		try:
			clientHubSocket = socket(AF_INET, SOCK_STREAM)
			print('Initiating TCP connection with server', serverName, 'over port', serverPort, '...')
			clientHubSocket.connect((serverName,serverPort))
			print('Closing TCP connection...')
			clientHubSocket.close()
			return True
		except:
			print('Could not make a connection to the server', serverPort)
			return False

	def run(self):
		"""
		Executa a lógica da thread
		"""
		serverPort = 12001
		hubSocket = socket(AF_INET,SOCK_STREAM)
		hubSocket.bind(('',serverPort))
		hubSocket.listen(1)
		print('The Hub is ready to receive from Servers')


		while 1:
			connectionSocket, addr = hubSocket.accept()
			print('Connected to server', addr)
			port = struct.unpack('i',connectionSocket.recv(4))[0]
			print('Port received:', port)
			if not self.contactServer(port):
				if port not in self.portsAvailable:
					self.portsAvailable.append(port)
				response = 'OK'
			else:
				print("Port", port,"is already available")
				response = "Port is already available"

			print("Ports available: ",self.portsAvailable)
			print()
			connectionSocket.send(response.encode())
			connectionSocket.close()


class ListenClient(Thread):
	"""
	Thread que escuta os clients que irão conectar com o hub.

	...

	Attributes
	----------
	num : int
		Numero da thread
	threadServers : ListenServers
		Objeto referente ao thread dos servidores

	"""

	def __init__(self, num, threadServers):
		"""
		Constroi todos os atributos e inicia o thread

		Parameters
		----------
		num : int
			Numero da thread
		threadServers : ListenServers
			Objeto referente ao thread dos servidores
		"""
		Thread.__init__(self)
		self.num = num
		self.threadServers = threadServers

	def servers_with_file(self, size_filename, filename, operation):
		"""
		Se conecta com os servidores disponíveis e verifica quais possuem um determinado arquivo

		Parameters
		----------
		size_filename : int
			Tamanho em bytes do nome do arquivo a ser procurado
		filename : str
			Nome do arquivo a ser procurado
		operation: int
			Operação executada pelo client
		
		Returns
		-------
		list of int
			Portas dos servidores conectados com o hub que possuem o arquivo
		"""
		servers = []
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
			clientHubSocket.send(struct.pack('i',size_filename))
			clientHubSocket.send(filename.encode())

			print('Waiting server response...')
			response = clientHubSocket.recv(3).decode()
			if response == 'ACK':
				print("Server", serverName, "in port", serverPort, "has the file", filename, ".")
				servers.append((serverName, serverPort))
				message = 'NCK'
				clientHubSocket.send(message.encode())
			else:
				print("Server", serverName, "in port", serverPort, "doesn't have the file", filename, ".")

			print('Closing TCP connection...')
			clientHubSocket.close()
			print('Finish.')

		return servers

	def add_files_to_servers(self, clientConnectionSocket, servers_with_file, size_filename, filename, ft_level):
		"""
		Recebe um arquivo do client e adiciona o mesmo nos servidores para atender a tolerância desejada

		Parameters
		----------
		clientConnectionSocket : socket
			Conexão com o socket do client
		servers_with_file : list of int
			Portas dos servidores conectados com o hub que possuem o arquivo
		size_filename : int
			Tamanho em bytes do nome do arquivo a ser adicionado
		filename : str
			Nome do arquivo a ser adicionado
		ft_level: int
			Nível de tolerância desejado
		
		Returns
		-------
		int
			Nível de tolerância alcançado
		"""
		print("Receiving file from Client...")
		file = open('temp','wb')
				
		packet = clientConnectionSocket.recv(1024)
		while (packet):
			file.write(packet)
			packet = clientConnectionSocket.recv(1024)

		file.close()

		for serverPort in self.threadServers.portsAvailable:
			serverName = 'localhost'
			if (serverName, serverPort) in servers_with_file:
				continue

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
			print('Sending filename.')
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

		return ft_level

	def remove_files_from_servers(self, servers_with_file, size_filename, filename, ft_level_remaining):
		"""
		Remove um determinado arquivo dos servidores conectados para atender a tolerância desejada

		Parameters
		----------
		servers_with_file : list of int
			Portas dos servidores conectados com o hub que possuem o arquivo
		size_filename : int
			Tamanho em bytes do nome do arquivo a ser removido
		filename : str
			Nome do arquivo a ser removido
		ft_level_remaining: int
			Nível de tolerância que falta para chegar no nível desejado
		
		Returns
		-------
		ft_level_remaining
			Nível de tolerância que falta para chegar no nível desejado
		"""
		for server in servers_with_file:
			try:
				clientHubSocket = socket(AF_INET, SOCK_STREAM)
				print('Initiating TCP connection with server', server[0], 'over port', server[1], '...')
				clientHubSocket.connect(server)
			except OSError:
				print('Could not make a connection to the server', server)
				print(OSError)
				continue

			print("Sending operation.")
			clientHubSocket.send(struct.pack('i', 3))

			print('Sending filename')
			clientHubSocket.send(struct.pack('i',size_filename))
			clientHubSocket.send(filename.encode())

			print('Waiting server response...')
			response = clientHubSocket.recv(3).decode()
			print(response)
			if response == 'ACK':
				print("Server", server[0], "in port", server[1], "erased the file", filename, ".")
				ft_level_remaining -= 1
			else:
				print("Server", server[0], "in port", server[1], "didn't erase the file", filename, ".")


			print('Closing TCP connection...')
			clientHubSocket.close()
			print('Finish.')
			print()
			if ft_level_remaining == 0:
				break

		return ft_level_remaining

	def recover_file(self, size_filename, filename):
		"""
		Recupera um arquivo dos servidores e salva-o em um arquivo temporario

		Parameters
		----------
		size_filename : int
			Tamanho em bytes do nome do arquivo a ser procurado
		filename : str
			Nome do arquivo a ser procurado
		
		Returns
		-------
		bool
			Estado da recuperação do arquivo
		"""
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

			print('Sending filename.')
			clientHubSocket.send(struct.pack('i',size_filename))
			clientHubSocket.send(filename.encode())

			print('Waiting server response...')
			response = clientHubSocket.recv(3).decode()
			if response == 'ACK':
				print("Server", serverName, "in port", serverPort, "has the file", filename, ".")
				print("Requesting the file from server...")
				request = 'ACK'
				clientHubSocket.send(request.encode())

				file_available = True
				try:
					file = open('temp','wb')
				except:
					print("Not possible to create the file")
					sys.exit(0)

				print("Receiving file from server...")
				packet = clientHubSocket.recv(1024)
				while (packet):
					file.write(packet)
					packet = clientHubSocket.recv(1024)
				file.close()
				print("File received.")
			else:
				print("Server", serverName, "in port", serverPort, "doesn't have the file", filename, ".")

			print('Closing TCP connection...')
			clientHubSocket.close()
			print('Finish.')

			if response == 'ACK':
				break

		return file_available

	def deposit(self, clientConnectionSocket, operation):
		"""
		Executa a lógica da operação "deposit" executada pelo client

		Parameters
		----------
		clientConnectionSocket : socket
			Conexão com o socket do client
		operation: int
			Operação executada pelo client

		Returns
		-------
		None
		"""
		size_filename = struct.unpack('i',clientConnectionSocket.recv(4))[0]
		filename = clientConnectionSocket.recv(size_filename).decode()
		print('Filename:', filename)
		ft_level = struct.unpack('i',clientConnectionSocket.recv(4))[0]
		print('Tolerance Level:', ft_level)
		print()

		servers_wf = self.servers_with_file(size_filename, filename, operation)
		print('Servers with file:',servers_wf)

		ft_level -= len(servers_wf)

		response = 'ACK'
		if ft_level <= 0:
			response = 'NCK'

		clientConnectionSocket.send(response.encode())

		if ft_level < 0:
			print('Actual Tolerance Level greater than requested.')
			print('Removing files from servers...')
			print()
			ft_level = self.remove_files_from_servers(servers_wf, size_filename, filename, -ft_level)
		elif ft_level > 0:
			print('Actual Tolerance Level smaller than requested.')
			print('Adding files to servers...')
			print()
			ft_level = self.add_files_to_servers(clientConnectionSocket, servers_wf, size_filename, filename, ft_level)

		if ft_level == 0:
			response = 'OK'
		else:
			response = 'Tolerance Level not accomplished: '+str(ft_level)
		
		clientConnectionSocket.send(response.encode())

	def recovery(self, clientConnectionSocket, operation):
		"""
		Executa a lógica da operação "recovery" executada pelo client

		Parameters
		----------
		clientConnectionSocket : socket
			Conexão com o socket do client
		operation: int
			Operação executada pelo client

		Returns
		-------
		None
		"""
		size_filename = struct.unpack('i',clientConnectionSocket.recv(4))[0]
		filename = clientConnectionSocket.recv(size_filename).decode()
		print("Filename:",filename)
		print()

		file_available = self.recover_file(size_filename, filename)
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

	def run(self):
		"""
		Executa a lógica da thread
		"""
		serverPort = 12000
		hubSocket = socket(AF_INET,SOCK_STREAM)
		hubSocket.bind(('',serverPort))
		hubSocket.listen(1)
		print('The Hub is ready to receive from Client')

		while 1:
			clientConnectionSocket, clientAddr = hubSocket.accept()
			try:
				print('Client connection accepted')
				operation = struct.unpack('i',clientConnectionSocket.recv(4))[0]
				print()
				if operation == 1:
					print('Deposit operation')
					print()
					self.deposit(clientConnectionSocket, operation)
				elif operation == 2:
					print('Recovery operation')
					print()
					self.recovery(clientConnectionSocket, operation)

				print()
				if os.path.exists('temp'):
					os.remove('temp')
				
				print("Closing connection with Client.")
				clientConnectionSocket.close()
			except Exception as e:
				print('An error ocurred:', e)
				print("Closing connection with Client.")
				print()
				clientConnectionSocket.close()

# Lógica do hub
if __name__ == "__main__":
	threadServers = ListenServers(1)
	threadServers.start()

	threadClient = ListenClient(1, threadServers)
	threadClient.start()

