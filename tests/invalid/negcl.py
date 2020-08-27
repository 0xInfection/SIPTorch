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
from core.utils import parseMsg, catMetHead

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Negative Content-Length',
    'id'        :   'negcl'
}

def negcl():
    '''
    Negative Content-Length

    This request has a negative value for Content-Length.

    An element receiving this message should respond with an error.  This
    request appeared over UDP, so the remainder of the datagram can
    simply be discarded.
    '''
    log = logging.getLogger('negcl')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the content length header
    head['Content-Length'] = '-%s' % random.getrandbits(10)
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run(sock):
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(sock, negcl()):
        log.info('Module %s completed' % module_info['test'])
