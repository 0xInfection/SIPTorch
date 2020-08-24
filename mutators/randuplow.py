#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random
import logging

def randUpLow(msg: str):
    '''
    Converts a string randomly between upper and lower case
    '''
    log = logging.getLogger('randUpLow')
    if not msg:
        log.error('Nothing available for transformation')
        return
    s = "".join(random.choice([k.upper(), k ]) for k in msg)
    return s
