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
from collections import defaultdict

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
    hd = defaultdict()
    for i in dc:
        hd[i.split(':')[0]] = i.split(':')[1]
    return hd


def ccatMetHead(req: str, headers: dict, body=r''):
    '''
    Converts a dict of headers to a SIP message
    '''
    if not (req or headers):
        return
    for header in headers.items():
        r += r'%s: %s\r\n' % header
    r += r'\r\n'
    r += body
    return r


def parseMsg(msg: str):
    '''
    Parses SIP messages into method line and header dict
    '''
    if msg is None:
        return
    mline, oth = msg.split(r'\r\n', 1)
    # If method is INVITE, we need to separate the body as well
    if "INVITE" in mline:
        header, body = oth.split(r'\r\n\r\n')
    else:
        header, body = oth, None
    
    # Parsing the header into a dict
    head = defaultdict()
    h = header.split(r'\r\n')
    h = [i.strip() for i in h]
    for i in h:
        head[i.split(':')[0]] = i.split(':')[1]
    return (mline, head, body)
