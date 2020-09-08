#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

from libs import config
import socket, logging, select, time
from core.requester.parser import parseResponse

def sockinit():
    '''
    Initiates a socket connection
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(config.TIMEOUT)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    return sock


def sendreq(sock, data):
    '''
    Sends the request to the server
    '''
    dst = (config.IP, config.RPORT)
    # Added delay functionality
    if config.DELAY > 0:
        time.sleep(config.DELAY)
    while data:
        # SIP RFC states the default serialized encoding is utf-8
        bytes_sent = sock.sendto(bytes(data[:8192], 'utf-8'), dst)
        data = data[bytes_sent:]


def handler(sock):
    '''
    Listens for incoming messages
    '''
    log = logging.getLogger('handler')
    bindingface = config.BIND_IFACE
    localport = config.LPORT
    # Descriptors to use during async I/O waiting
    rlist = [sock]
    wlist, xlist = list(), list()
    log.debug("binding to %s:%s" % (bindingface, config.LPORT))
    try:
        sock.bind((bindingface, localport))
    except socket.error as err:
        pass
    while True:
        data, *_ = select.select(rlist, wlist, xlist, config.TIMEOUT)
        if data:
            buff, src = sock.recvfrom(8192)
            daff, host, port = parseResponse(buff, src)
            log.debug("Data received from: %s:%s" % (str(host), str(port)))
            return (daff, host, port)
        else:
            try:
                buff, src = sock.recvfrom(8192)
                daff, host, port = parseResponse(buff, src)
                log.debug("Data received from: %s:%s" % (str(host), str(port)))
                return (daff, host, port)
            except socket.timeout:
                log.error('Timeout occured when waiting for message')
                return ('Generic Timeout Occured - No Response Received\nInvestigate your server logs.', '', '')
            except socket.error as err:
                log.error("Target %s errored out: %s" % (str(host), err.__str__()))
                return ('Error Enountered: %s' % err.__str__(), '', '')
