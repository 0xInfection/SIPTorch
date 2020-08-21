#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import socket, logging, select
from core.requester.parser import parseResponse
from core.config import TIMEOUT, BIND_IFACE, LPORT

def sockinit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(TIMEOUT)
    sock.setsockopt(socket.SOL_SOCKET, socket.SOL_SOCKET, 1)
    return sock

def sendreq(sock, data, dst):
    '''
    Sends the request to the server
    '''
    while data:
        # SIP RFC states the default serialized encoding is utf-8
        bytes_sent = sock.sendto(bytes(data[:8192], 'utf-8'), dst)
        data = data[bytes_sent:]

def handler(sock):
    log = logging.getLogger('handler')
    bindingface = BIND_IFACE
    localport = LPORT
    # Descriptors to use during async I/O waiting
    rlist = [sock]
    wlist, xlist = list(), list()
    log.debug("binding to %s:%s" % (bindingface, LPORT))
    try:
        sock.bind((bindingface, localport))
    except socket.error:
        log.critical("cannot bind to %s" % localport)
    while True:
        data, *_ = select.select(rlist, wlist, xlist, TIMEOUT)
        if data:
            try:
                buff, src = sock.recvfrom(8192)
                data, host, port = parseResponse(buff, src)
                log.debug("Data received from: %s:%s" % (str(host), str(port)))
                log.debug("Data: \n%s" % data)
            except socket.error as err:
                log.error("Target %s errored out: %s" % (str(host), err.__str__))
    return (data, host, port)