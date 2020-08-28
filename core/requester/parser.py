#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import socket, logging
from core.config import RPORT
from libs.data import RESP_MAP, BAD_RESP

def parseResponse(buff, addr):
    '''
    Figuring out the SIP response
    '''
    log = logging.getLogger("parseResponse")
    if not (buff or addr):
        log.error("Nothing available for parsing")
        return
    ip, port, *_ = addr
    # Decoding the buffer in response
    data = buff.decode('utf-8', 'ignore')
    return (data, str(ip), str(port))

def validateHost(url: str):
    '''
    Validating a host to be a proper host and not some random junk string
    '''
    log = logging.getLogger('validateHost')
    log.info('Trying to validate host')
    try:
        socket.inet_aton(url)
        log.info('Input seems to be a IP address')
        if lookUp(url):
            return url
        else:
            log.critical('Target %s not responding on port %s' % (url, RPORT)) 
            return
    except OSError:
        log.info('The input does not seem to be a IP, must be a domain')
        ip = lookUp(url, typef='domain')
        if ip:
            log.info("%s resolves to %s" % (url, ip))
            return ip
        else: return 

def lookUp(url: str, typef='ip', port=RPORT):
    '''
    Looks up domains and ip for validity
    '''
    log = logging.getLogger('lookUp')
    # Checking for TCP support, might be useful for future support
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        if typef == 'ip':
            if s.connect_ex((url, port)) == 0:
                log.info('Valid IP detected')
                return True
            else: return
        else:
            ip = socket.gethostbyname(url)
            return ip
    except socket.error as err:
        log.critical("Socket errored out with: %s" % err.__str__())
        return

def checkBadResponse(msg: str):
    '''
    Check the response received. If the response received is a bad response/waiting response
    keep waiting for a original message.
    '''
    for x in BAD_RESP:
        st = 'SIP/2.0 %s' % x
        if msg.startswith(st):
            return True
    return False