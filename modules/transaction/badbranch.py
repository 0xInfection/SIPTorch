#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, re
from core.plugrun import runPlugin
from core.requester import buildreq
from core.requester.parser import parseMsg, catMetHead
from mutators.replparam import rmallParam, rmspcParam

module_info = {
    'category'  :   'Transaction Layer Semantics',
    'test'      :   'Branch Tag Missing Transaction Identifier',
    'id'        :   'badbranch'
}

def badbranch():
    '''
    Branch Tag Missing Transaction Identifier

    This request indicates support for RFC 3261-style transaction
    identifiers by providing the z9hG4bK prefix to the branch parameter,
    but it provides no identifier.  A parser must not break when
    receiving this message.  An element receiving this request could
    reject the request with a 400 Response (preferably statelessly, as
    other requests from the source are likely also to have a malformed
    branch parameter), or it could fall back to the RFC 2543-style
    transaction identifier.
    '''
    log = logging.getLogger('badbranch')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Remove the branch identifier after z9hG4bk
    repl = re.sub(r'z9hG4bK.*?[^;]*', r'z9hG4bK', head['Via'])
    head['Via'] = repl
    # Forming the request message back up
    msg = catMetHead(mline, head, body=body)
    return msg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(badbranch(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
