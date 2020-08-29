#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from libs.data import LONGSHORT_MAP

def convShort(header: dict, convrand=False, specific=''):
    '''
    Converts long form of SIP addresses to short
    '''
    log = logging.getLogger('convshort')
    mapping = LONGSHORT_MAP
    log.debug('Converting headers into short form')
    if not header:
        log.error('Nothing available for parsing')
        return
    if specific:
        header[mapping[specific.lower()]] = header.pop(specific)
        return header
    head = header.copy()
    # If the convrand is set to false we convert all headers
    # Leaving the other part for later as now we don't need it.
    # TODO: If convrand is True, we need to pick random headers
    # from the header dict and then convert them, again merge the
    # final with original dict.
    if not convrand:
        for k in head.keys():
            if k.lower() in mapping:
                header[mapping[k.lower()]] = header.pop(k)
        return header



