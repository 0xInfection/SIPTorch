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
from core.utils import parseMsg, catMetHead

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Unterminated Quoted String in Display Names',
    'id'        :   'balquote'
}

def balquote():
    '''
    Unterminated Quoted String in Display Names

    This is a request with an unterminated quote in the display name of
    the To field.  An element receiving this request should return a 400
    Bad Request error.
    '''
    log = logging.getLogger('balquote')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Remove second quote in the to and from headers
    head['From'] = ''.join(head.get('From').rsplit('"', 1))
    head['To'] = ''.join(head.get('To').rsplit('"', 1))
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run(sock):
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(sock, balquote()):
        log.info('Module %s completed' % module_info['test'])
