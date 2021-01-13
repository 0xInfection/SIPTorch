#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, random
from core.plugrun import runPlugin
from core.requester import buildreq
from core.requester.parser import parseSIPMessage, concatMethodxHeaders
from mutators.replparam import genRandStr
from mutators.replparam import rmallParam, rmspcParam

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Response with Overlarge Status Code',
    'id'        :   'bigcode'
}

def bigcode():
    '''
    Response with Overlarge Status Code

    This response has a response code larger than 699. An element
    receiving this response should simply drop it.
    '''
    log = logging.getLogger('bigcode')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseSIPMessage(msg)
    # Tweak 1: Modify the method line
    mline = 'SIP/2.0 %s %s' % (random.getrandbits(32), genRandStr(20))
    # Forming the request message back up
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(bigcode(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
