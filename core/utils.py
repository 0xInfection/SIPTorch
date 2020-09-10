#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import os
import sys
import socket
import random
import logging
import subprocess
from libs import config
from libs.data import BAD_RESP

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
            log.critical('Target %s not responding on port %s' % (url, config.RPORT)) 
            return
    except OSError:
        log.info('The input does not seem to be a IP, must be a domain')
        ip = lookUp(url, typef='domain')
        if ip:
            log.info("%s resolves to %s" % (url, ip))
            return ip
        else: return 


def lookUp(url: str, typef='ip', port=config.RPORT):
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


def calcLogLevel(args):
    '''
    Calculate logging level based on verbose options
    '''
    baseloglevel = config.DEBUG_LEVEL
    if args.verbose is not None:
        if args.verbose >= 3:
            baseloglevel = 10
        else:
            baseloglevel = 30 - (args.verbose * 10)
    if args.quiet:
        baseloglevel = 50
    return baseloglevel


def clsterm(content: str):
    '''
    Clears terminal and then prints out the content
    '''
    _ = subprocess.call('clear' if os.name =='posix' else 'cls')
    print(content)
    return