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
from core.utils import parseMsg, catMetHead

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'OPTIONS Request URI with Unknown Scheme',
    'id'        :   'unkscm'
}

def unkscm():
    '''
    OPTIONS Request URI with Unknown Scheme

    This OPTIONS contains an unknown URI scheme in the Request-URI.  A
    parser must accept this as a well-formed SIP request.

    An element receiving this request will reject it with a 416
    Unsupported URI Scheme response.

    Some early implementations attempt to look at the contents of the To
    header field to determine how to route this kind of request.  That is
    an error.  Despite the fact that the To header field and the Request
    URI frequently look alike in simplistic first-hop messages, the To
    header field contains no routing information.
    '''
    log = logging.getLogger('unkscm')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseMsg(msg)
    # Tweak 1: modify the request URI scheme
    mline = mline.replace(mline.split(' ')[1], 'unknownscheme:unknowncontent')
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg

def run(sock):
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(sock, unkscm()):
        log.info('Module %s completed' % module_info['test'])
