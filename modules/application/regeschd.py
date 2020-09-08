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
from core.requester.parser import parseMsg, catMetHead

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'REGISTER with a URL Escaped Header',
    'id'        :   'regeschd'
}

def regeschd():
    '''
    REGISTER with a URL Escaped Header

    This register request contains a contact where the URI has an escaped
    header.

    The register should succeed, and a subsequent retrieval of the
    registration must include the escaped Route header in the contact URI
    for this binding.
    '''
    log = logging.getLogger('regeschd')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('REGISTER')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Contact header where URI has escaped header
    head['Contact'] += r'?Route=%3Csip:sip.example.com%3E'
    head['Contact'] = '<%s>' % head['Contact']
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(regeschd(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
