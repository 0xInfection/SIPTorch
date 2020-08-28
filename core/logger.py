#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import datetime
import os, logging, sys
from core.config import OUTPUT_DIR, RHOST, IP, RPORT, DEF_EXT

def checkDir():
    '''
    Check if directories are present and create 
    the output locations
    '''
    global host
    host = RHOST
    if not RHOST:
        host = IP
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
    if os.path.exists(dirc+host+'.md'):
        log.critical('Report for this site already exists')
        sys.exit('Exiting...')
    return dirc

global dirc
dirc = checkDir() + host + '.md'

def loggerinit():
    '''
    Module to get stuff together
    '''
    s = '''# SIPTorch Report

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

def logfooter(start, end):
    '''
    Add footer info
    '''
    content = '''## Benchmarks:
- __Date:__ %s
- __Start Time:__ %s
- __End Time:__ %s
- __Total Time Taken:__ %s
''' % ( datetime.datetime.now().strftime('%x'), 
        start, end, (end-start) )
    with open(dirc, 'a', encoding='utf-8', newline='\n') as f:
        f.write(content+'\n')