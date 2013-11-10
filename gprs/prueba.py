#!/usr/bin/env python
# encoding: utf-8
"""
Cliente.py

Created by José Andrés Ayestarán Irarrázaval.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import socket
import time
import threading


class MiThread(threading.Thread):
    def __init__(self, imei):
        threading.Thread.__init__(self)
        self.socket = socket.socket()
        self.data = "$$B03597720360"
    def run(self):
        self.socket.connect(("54.204.30.71", 3000))
        t = 0
        while t<20:
            data = self.data + str(t)
            self.socket.send(data)
            t+=1
            time.sleep(5)
        self.socket.close()


def main():
    number = 1
    s = MiThread(number)
    s.start()



if __name__ == '__main__':
    main()

