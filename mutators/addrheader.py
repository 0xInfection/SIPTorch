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

def addRandHeader(head: dict):
    '''
    Add random headers to the default header set
    '''
    log = logging.getLogger('addRandHeader')
    if not head:
        log.error('No message supplied for performing mutation')
        return
    log.info('Applying addRandHeader transformation')
    # Merging two dicts in
    try:
        # for versions >= 3.5
        fhead = { **head, **EXT_HEADERS }
    except Exception:
        fhead = head.copy()
        fhead.update(EXT_HEADERS)
    return fhead