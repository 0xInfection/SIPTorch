#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging

def convshort(header: dict, convrand=False):
    '''
    Converts long form of SIP addresses to short
    '''
    # Lowercase version helps better avoiding false postives
    mapping = {
        'accept-contact'    :   'a',
        'referred-by'       :   'b',
        'content-type'      :   'c',
        'content-encoding'  :   'e',
        'from'              :   'f',
        'call-id'           :   'i',
        'supported'         :   'k',
        'content-length'    :   'l',
        'contact'           :   'm',
        'event'             :   'o',
        'refer-to'          :   'r',
        'subject'           :   's',
        'to'                :   't',
        'allow-events'      :   'u',
        'via'               :   'v'
    }
    log = logging.getLogger('convshort')
    log.debug('Converting headers into short form')
    if not header:
        log.error('Nothing available for parsing')
        return
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



