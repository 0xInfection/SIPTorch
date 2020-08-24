#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, random
from core.requester import buildreq
from core.utils import parseMsg, catMetHead
from mutators.replparam import genRandStr

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'OPTIONS With Unknown Proxy-Require and Require Scheme',
    'id'        :   'reqpreq'
}

def reqpreq():
    '''
    Require & Proxy-Require Implementation Stress
    '''
    log = logging.getLogger('reqpreq')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Add Require & Proxy-Require fields
    head['Require'] = '%s, %s' % (genRandStr(10), random.getrandbits(32))
    head['Proxy-Require'] = '%s, %s' % (genRandStr(10), genRandStr(20))
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg
