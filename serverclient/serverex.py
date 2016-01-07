#!/usr/bin/python

import eventlet


def handle(connect):
    while 1:
        c = connect.recv(1024)
        if not c:
            print 'not c'
        print c
        connect.sendall('Thanks for data. I got it')

server = eventlet.listen(('0.0.0.0', 6000))

pool = eventlet.GreenPool(1000)

while True:
    new_sock, address = server.accept()
    print new_sock
    print type(new_sock)
    print address
    pool.spawn_n(handle, new_sock)
    eventlet.greenthread.sleep(0.00001)
