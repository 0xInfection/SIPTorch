#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import os, logging
from core.config import (
    OUTPUT_DIR, 
    RHOST, 
    IP,
    RPORT,
    DEF_EXT
)

def checkDir():
    '''
    Check if directories are present and create 
    the output locations
    '''
    log = logging.getLogger('checkDir')
    dirc = OUTPUT_DIR
    if not dirc.endswith('/'):
        dirc += '/'
    try:
        if not os.path.exists(dirc):
            log.debug('Creating the directory')
            os.makedirs(dirc)
    except FileExistsError:
        log.error('Directory %s already exists' % dirc)
        return dirc
    return dirc

def loggerinit():
    '''
    Module to get stuff together
    '''
    host = RHOST
    if not RHOST:
        host = IP
    # First we check if directory already exists
    global dirc
    # We do markdown format
    dirc = checkDir() + host + '.md'
    s = '''
# SIPTorch Report

## Target Specifications:
- __Target:__ %s
- __IP:__ %s
- __Port:__ %s
- __Extension:__ %s

## Tests:
    ''' % (RHOST, IP, RPORT, DEF_EXT)
    # Creating the file now
    with open(dirc, 'w+', encoding='utf-8', newline='\n') as f:
        f.write(s)


def logresp(content):
    '''
    Log response to a file 
    '''
    log = logging.getLogger('logresp')
    try:
        with open(dirc, 'a', encoding='utf-8', newline='\n') as f:
            f.write(content+'\n')
    except Exception as e:
        log.error("Error: %s" % e.__str__())