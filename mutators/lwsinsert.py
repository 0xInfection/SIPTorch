#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random, logging
from libs.chars import (
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

def lwsInsert(msg: str, charc='random'):
    '''
    Inserts random characters into strings randomly.
    By default it inserts whitespaces, but you can use a string too.
    '''
    log = logging.getLogger('lwsInsert')
    if not msg:
        log.error('No message supplied for performing mutation')
        return
    wschars = [TAB, EN_QUAD, EM_QUAD, WS, IDG_SEP]
    # Generate the character sequence
    if charc is 'random':
        # Fetching all whitespace chars
        log.debug('Performing random LWS mutation')
        return ''.join('%s%s' % (x, random.choice((random.choice(wschars), ""))) for x in msg)
    else:
        log.debug('Performing single LWS mutation')
        return ''.join('%s%s' % (x, random.choice((charc, ""))) for x in msg)
    