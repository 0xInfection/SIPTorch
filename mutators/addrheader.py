#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from core.config import EXT_HEADERS
from core.utils import parseMsg, ccatMetHead

def addRandHeader(msg: str):
    '''
    Add random headers to the default header set
    '''
    log = logging.getLogger('addRandHeader')
    if not msg:
        return
    mline, head, body = parseMsg(msg)
    # Merging two dicts in
    try:
        # for versions >= 3.5
        fhead = { **head, **EXT_HEADERS }
    except Exception:
        fhead = head.copy()
        fhead.update(EXT_HEADERS)
    # Reforming the final message
    fmsg = ccatMetHead(mline, fhead, body=body)
    return fmsg