#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import socket, logging
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


def concatMethodxHeaders(req: str, headers: dict, body=r''):
    '''
    Converts a request line, dict of headers, body to a SIP message
    '''
    if not (req or headers):
        return
    if '\r\n' not in req:
        req += '\r\n'
    for header in headers.items():
        req += '%s: %s\r\n' % header
    req += '\r\n'
    req += body
    return req


def parseSIPMessage(msg: str):
    '''
    Parses SIP messages into method line and header dict
    '''
    log = logging.getLogger('parseSIPMessage')
    if msg is None:
        log.error("No message for parsing")
        return
    mline, oth = msg.split('\r\n', 1)
    header, body = oth.split('\r\n\r\n')
    # Parsing the header into a dict
    head = dict()
    h = header.split('\r\n')
    h = [i.strip() for i in h]
    for i in h:
        head[i.split(':', 1)[0]] = i.split(':', 1)[1].strip()
    return (mline, head, body)