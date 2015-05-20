#!/usr/bin/python

import socket, thread, sqlite3
from time import strftime, localtime

class IRCClient(object):
    def __init__(self):
		self.test = 1

    def connect(self, server, port):
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.connect((server, port))
        self._send("NICK "+self.__user['nick'])
        self._send("USER "+self.__user['user']+" localhost * :Python Searchbot")

        #thread.start_new_thread(self._listen, (self,))
        self._listen()
