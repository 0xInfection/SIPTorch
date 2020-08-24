#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import sys
import random
import logging

def genCombinations(lst, LW_CONST=3, UP_CONST=7):
    '''
    Takes in a list and generates combination of those chars to form a string
    '''
    # Generating random combinations
    s = ""
    for _ in range(random.randint(LW_CONST, UP_CONST)):
        s += random.choice(lst)
    return s


def readHeader(temp: str):
    '''
    Read a template file to form a SIP header dict
    '''
    log = logging.getLogger('readHeader')
    try:
        with open(temp, 'r') as f:
            dc = f.read().splitlines()
            dc = [i.strip() for i in dc]
    except (FileNotFoundError, OSError):
        log.error('File "%s" not found.' % temp)
        return
    hd = dict()
    for i in dc:
        hd[i.split(':')[0]] = i.split(':')[1]
    return hd


def catMetHead(req: str, headers: dict, body=r''):
    '''
    Converts a dict of headers to a SIP message
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


def parseMsg(msg: str):
    '''
    Parses SIP messages into method line and header dict
    '''
    log = logging.getLogger('parseMsg')
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


def fileWriter(f, test, addr, data):
    '''
    Writes stuff to a file
    '''
    log = logging.getLogger('fileWriter')
    host, port, *_ = addr
    log.debug("Writing data for test: %s" % test)
    with open(f, 'w+') as xwrt:
        xwrt.write('[+] Test: %s' % test)
        xwrt.write('[+] Address: %s:%s' % (str(host), str(port)))
        xwrt.write('[+] Response: \n%s' % data.decode('utf-8', 'ignore'))
    log.debug("Successfully written to %s" % f)