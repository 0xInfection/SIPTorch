#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, random
from libs.chars import BACKSLASH_SEQ1, BACKSLASH_SEQ2

def insertBkSlash(msg: str):
    '''
    Insert backslash before the ending double quote
    '''
    log = logging.getLogger('insertBkSlash')
    if not msg:
        log.error("Nothing to apply transformation to")
        return
    if "\"" in msg:
        # Replacing at the second occurance
        seq = random.choice([BACKSLASH_SEQ1, BACKSLASH_SEQ2])
        s = msg.replace('"', seq, 2).replace(seq, '"', 1)
    return s
