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
from core.config import BIND_IFACE, LPORT, TIMEOUT, IP, RPORT

def sockinit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(TIMEOUT)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    return sock

def sendreq(sock, data):
    '''
    Sends the request to the server
    '''
    dst = (IP, RPORT)
    while data:
        # SIP RFC states the default serialized encoding is utf-8
        bytes_sent = sock.sendto(bytes(data[:8192], 'utf-8'), dst)
        data = data[bytes_sent:]

def handler(sock):
    log = logging.getLogger('handler')
    bindingface = BIND_IFACE
    localport = LPORT
    host = IP
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
            buff, src = sock.recvfrom(8192)
            daff, host, port = parseResponse(buff, src)
            log.debug("Data received from: %s:%s" % (str(host), str(port)))
            log.debug("Data: \n%s" % daff)
            return (daff, host, port)
        else:
            try:
                buff, src = sock.recvfrom(8192)
                daff, host, port = parseResponse(buff, src)
                log.debug("Data received from: %s:%s" % (str(host), str(port)))
                log.debug("Data: \n%s" % daff)
                return (daff, host, port)
            except socket.timeout as err:
                log.error('Timeout occured when waiting for message: %s' % err.__str__())
                return ('Generic Timeout Occured - No Response Received', '', '')
            except socket.error as err:
                log.error("Target %s errored out: %s" % (str(host), err.__str__()))
                return ('Error Enountered: %s' % err.__str__(), '', '')
