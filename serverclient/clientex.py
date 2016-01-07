#!/usr/bin/python

import eventlet
from eventlet.green import socket

try:
    s = socket.socket()
    s.connect(('0.0.0.0', 6000))
except Exception as e:
    print e

while True:
    try:
        info = s.sendall('hehehe')
        print info
        data = s.recv(1024)
        print data
        eventlet.greenthread.sleep(1)
    except Exception as e:
        s.close()
        print e
        break
