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
from core.plugrun import runPlugin
from core.requester.parser import parseMsg, catMetHead

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   '200 OK Response with Broadcast Via Header Field Value',
    'id'        :   'bcast'
}

def bcast():
    '''
    200 OK Response with Broadcast Via Header Field Value

    The message is well formed; parsers must not fail when receiving 
    it. An endpoint receiving this message should simply discard it.

    If a proxy followed normal response processing rules blindly, it
    would forward this response to the broadcast address.  To protect
    against this as an avenue of attack, proxies should drop such
    responses.
    '''
    bcastaddr = '255.255.255.255'
    log = logging.getLogger('bcast')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: The message header first
    mline = 'SIP/2.0 200 OK'
    # Tweak 2: Add another via header
    head['via'] = 'SIP/2.0/UDP %s;branch=z9hG4bK-%s' % (bcastaddr, random.getrandbits(32))
    # Recompiling our message
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(bcast(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
