#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random, logging
from libs.data import (
    TAB,
    EM_QUAD,
    EN_QUAD,
    WS,
    IDG_SEP
)

# Upper costraint
UP_CONST = 7
# Lower constraint
LW_CONST = 3

def lwsInsert(msg: str, length=3, crlf=False, charc='random', endsonly=False):
    '''
    Inserts LWS into strings based on options available.
    Can also input CRLF sequences at positions for mutating strings. 
    '''
    log = logging.getLogger('lwsInsert')
    if not msg:
        log.error('No message supplied for performing mutation')
        return
    wschars = [TAB, EN_QUAD, EM_QUAD, WS, IDG_SEP]
    if endsonly:
        log.debug('Performing ends-only LWS mutation')
        s = msg.replace(' ', (random.choice(wschars)*length))
    # If charc is random then, we randomly insert chars
    if charc == 'random':
        log.debug('Performing random LWS mutation')
        s = ''.join('%s%s' % (x, random.choice((
            random.choice(wschars), ""))) for x in msg)
    if crlf:
        log.debug('Applying CRLF transformation')
        for x in s:
            if x in wschars:
                s = s.replace(x, x+'\r\n'+x) if random.random() > 0.9 else s
    return s
