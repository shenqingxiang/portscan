# -*- coding:utf-8 -*-
import socket
from multiprocessing.dummy import Pool as ThreadPool

socket.setdefaulttimeout(0.5)

host = ''


def get_remote_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.error, e:
        print '%s: %s' % (domain, e)
    return 0


def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = s.connect_ex((host, port))
    if res == 0:
        print 'Port {}, open.'.format(port)


if __name__ == '__main__':
    pool = ThreadPool(8)
    pool.map(scan, [x for x in range(1, 10000)])
    pool.close()
    pool.join()