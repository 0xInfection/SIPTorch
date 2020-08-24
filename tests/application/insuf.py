#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from core.requester import buildreq
from core.utils import parseMsg, catMetHead
from mutators.replparam import rmallParam, rmspcParam

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'INVITE Message Missing Required Header Fields',
    'id'        :   'insuf'
}

def insuf():
    '''
    INVITE Message Missing Required Header Fields
    '''
    log = logging.getLogger('insuf')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Remove the following required headers
    rmhead = ('Call-ID', 'From', 'To')
    for x in rmhead:
        head.pop(x, None)
    # Tweak 2: Adding a random header
    head['1'] = '152'
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg
