#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import datetime, time
import os, logging, sys
from core.colors import C, R, G
from core.config import OUTPUT_DIR, RHOST, IP, RPORT, DEF_EXT

class CustomFormatter(logging.Formatter):
    '''
    Customising my style of logging the results
    '''
    err_fmt  = R+" ERROR: %(msg)s"
    crt_fmt  = R+" CRITICAL: %(msg)s"
    dbg_fmt  = C+" DEBUG: %(module)s: %(msg)s"
    info_fmt = G+" %(msg)s"

    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(msg)s", datefmt=None, style='%')  
    
    def format(self, record):

        format_orig = self._style._fmt

        if record.levelno == logging.DEBUG:
            self._style._fmt = CustomFormatter.dbg_fmt

        elif record.levelno == logging.INFO:
            self._style._fmt = CustomFormatter.info_fmt

        elif record.levelno == logging.ERROR:
            self._style._fmt = CustomFormatter.err_fmt

        elif record.levelno == logging.CRITICAL:
            self._style._fmt = CustomFormatter.crt_fmt

        result = logging.Formatter.format(self, record)
        self._style._fmt = format_orig

        return result

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
        s = input(C+' Run tests again? (Y/n) :> ')
        if not s or s.lower() == 'y':
            pass
        else:
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
    return


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
- __Total Time Taken:__ %ss
''' % ( datetime.datetime.now().strftime('%a, %d %b %Y'), 
        time.strftime("%H:%M:%S %Z", time.localtime(start)), 
        time.strftime("%H:%M:%S %Z", time.localtime(end)), 
        '%.3f' % (end-start) )
    with open(dirc, 'a', encoding='utf-8', newline='\n') as f:
        f.write(content+'\n')