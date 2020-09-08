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
    'test'      :   'Malformed SIP Request-URI with Embedded LWS',
    'id'        :   'lwsuri'
}

def lwsuri():
    '''
    Malformed SIP Request-URI with Embedded LWS

    This INVITE has illegal LWS within the Request-URI. An element receiving
    this request should respond with a 400 Bad Request.
    '''
    log = logging.getLogger('lwsuri')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Insert lws after the URI element
    requri = mline.split(' ')[1]
    requri += r'; somerandomparamter'
    mline = mline.replace(mline.split(' ')[1], requri)
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(lwsuri(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
