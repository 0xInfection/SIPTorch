#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from mutators.permcase import permuteCase

def multiHead(msg: str, permuteasdict=True, singlestr=False, lent=2):
    '''
    Multiplies a string n times to enlargen field
    msg: can be either str or dict
    '''
    log = logging.getLogger('multiHead')
    if not msg:
        log.error('Nothing available for parsing')
        return
    # if msg is str, singlestr will be True
    if singlestr:
        s = msg*lent
        return s
    # if msg is dict, then permute the key sent alongside
    if permuteasdict:
        log.debug('Generating maximum permutations for header: %s' % msg)
        d = permuteCase(msg)
        s = { s : '' for s in d }
    return s
