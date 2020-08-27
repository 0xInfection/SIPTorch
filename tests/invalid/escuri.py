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
    'test'      :   'Escaped Headers in SIP Request-URI',
    'id'        :   'escuri'
}

def escuri():
    '''
    Escaped Headers in SIP Request-URI

    This INVITE is malformed, as the SIP Request-URI contains escaped
    headers.

    It is acceptable for an element to reject this request with a 400 Bad
    Request. An element could choose to be liberal in what it accepts
    and ignore the escaped headers. If the element is a proxy, the
    escaped headers must not appear in the Request-URI of the forwarded
    request (and most certainly must not be translated into the actual
    header of the forwarded request).
    '''
    log = logging.getLogger('escuri')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the header
    newrequri = mline.split(' ')[1]
    newrequri += r'?Route=%3Csip:example.com%3E'
    mline = mline.replace(mline.split(' ')[1], newrequri)
    mg = catMetHead(mline, head, body=body)
    return mg

def run(sock):
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(sock, escuri()):
        log.info('Module %s completed' % module_info['test'])
