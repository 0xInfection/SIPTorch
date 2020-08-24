#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging

def multiHead(msg: str, lent=2):
    '''
    Multiplies a string n times to enlargen field
    '''
    log = logging.getLogger('multiHead')
    if not msg:
        log.error('Nothing available for parsing')
        return
    s = msg*lent
    return s
