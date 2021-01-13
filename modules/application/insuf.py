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
from core.plugrun import runPlugin
from core.requester.parser import parseSIPMessage, concatMethodxHeaders

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'INVITE Message Missing Required Header Fields',
    'id'        :   'insuf'
}

def insuf():
    '''
    INVITE Message Missing Required Header Fields

    This request contains no Call-ID, From, or To header fields.

    An element receiving this message must not break because of the
    missing information.  Ideally, it will respond with a 400 Bad Request
    error.
    '''
    log = logging.getLogger('insuf')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseSIPMessage(msg)
    # Tweak 1: Remove the following required headers
    rmhead = ('Call-ID', 'From', 'To')
    for x in rmhead:
        head.pop(x, None)
    # Tweak 2: Adding a random header
    head['Content-Length'] = '152'
    # Forming the request message back up
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(insuf(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
