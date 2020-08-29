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
from core.requester.parser import parseMsg, catMetHead

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Failure to Enclose name-addr URI in <>',
    'id'        :   'reginvct'
}

def reginvct():
    '''
    Failure to Enclose name-addr URI in <>

    This REGISTER request is malformed.  The SIP URI contained in the
    Contact Header field has an escaped header, so the field must be in
    name-addr form (which implies that the URI must be enclosed in <>).

    It is reasonable for an element receiving this request to respond
    with a 400 Bad Request.  An element choosing to be liberal in what it
    accepts could infer the angle brackets since there is no ambiguity in
    this example.  In general, that won't be possible.
    '''
    log = logging.getLogger('reginvct')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the contact header, and leave it just 
    # like that, not adding any < or > around URL
    head['Contact'] += r'?Route=%3Csip:sip.example.com%3E'
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(reginvct(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
