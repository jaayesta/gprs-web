#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by José Andrés Ayestarán Irarrázaval on 2013-11-19.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import time
import socket

HOST = "54.204.30.71"
PORT = 3000

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	print 'Connected with server %s at port %s' % (HOST, PORT)
	t = 0
	while t < 20:
		data = 'Dato#%s' % (t)
		s.send(data)
		t+=1
		time.sleep(5)
	s.close()
	print 'Socket closed'

if __name__ == '__main__':
	main()

