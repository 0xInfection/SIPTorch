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
    'category'  :   'Syntactical Parser Tests',
    'test'      :   'Message with No LWS between Display Name and <',
    'id'        :   'lwsdp'
}

def lwsdp():
    '''
    Message with No LWS between Display Name and <

    This OPTIONS request is not valid per the grammar in RFC 3261 since
    there is no LWS between the token in the display name and < in the
    From header field value.  This has been identified as a specification
    bug that will be removed when RFC 3261 is revised.  Elements should
    accept this request as well formed.
    '''
    log = logging.getLogger('lwsdp')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseSIPMessage(msg)
    # Tweak 1: Remove LWS between from and to
    head['From'] = head.get('From').replace(' ', '')
    head['To'] = head.get('To').replace(' ', '')
    # Forming the message up back again
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(lwsdp(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
