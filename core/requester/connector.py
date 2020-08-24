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
from core.config import BIND_IFACE, LPORT, TIMEOUT

def sockinit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(TIMEOUT)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
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
    except socket.error as err:
        pass
    while True:
        data, *_ = select.select(rlist, wlist, xlist, TIMEOUT)
        if data:
            try:
                buff, src = sock.recvfrom(8192)
                daff, host, port = parseResponse(buff, src)
                log.debug("Data received from: %s:%s" % (str(host), str(port)))
                log.debug("Data: \n%s" % daff)
                break
            except socket.error as err:
                log.error("Target %s errored out: %s" % (str(host), err.__str__))
    return (daff, host, port)
