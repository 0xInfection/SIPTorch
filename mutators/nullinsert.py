#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random, logging
from libs.data import NULL_CHAR

# Upper costraint
UP_CONST = 7
# Lower constraint
LW_CONST = 3

def nullInsert(msg: str, lent=1):
    '''
    Inserts random null chars into strings randomly.
    '''
    log = logging.getLogger('nullInsert')
    if not msg:
        log.error('No message supplied for performing mutation')
        return
    chard = NULL_CHAR * lent
    return ''.join('%s%s' % (x, 
        random.choice((chard, ""))) for x in msg)
