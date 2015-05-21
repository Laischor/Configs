#!/usr/bin/python

import socket, thread, sqlite3
from time import strftime, localtime

class Server(object):
	def __init__(self):
		self.test = 1

	def start(self):
		self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__s.bind(('', 1337))

        #thread.start_new_thread(self._listen, (self,))
		self.__s.listen(10)

		print 'Server started!'

		while 1:
			conn, addr = self.__s.accept()
			print 'Connected with ' + addr[0] + ':' + str(addr[1])

		self.__s.close();

test = Server();
test.start();
