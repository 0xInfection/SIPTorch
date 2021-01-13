#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from core.plugrun import runPlugin
from core.requester import buildreq
from core.requester.parser import parseSIPMessage, concatMethodxHeaders

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Escaped Headers in SIP Request-URI',
    'id'        :   'trws'
}

def trws():
    '''
    SP Characters at End of Request-Line

    This OPTIONS request contains SP characters between the SIP-Version
    field and the CRLF terminating the Request-Line.

    It is acceptable to reject this request as malformed.  An element
    that is liberal in what it accepts may ignore these extra SP
    characters when processing the request.  If the element forwards the
    request, it must not include these extra SP characters in the
    messages it sends.
    '''
    log = logging.getLogger('trws')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseSIPMessage(msg)
    # Tweak 1: Add a non-ascii utf junk at the end of req. line
    mline = mline.strip('\r\n')
    # Using the 0x00002020 as a junk char
    mline += bytearray.fromhex('2020').decode('utf-8')
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(trws(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
