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
from mutators.replparam import rmallParam, rmspcParam

module_info = {
    'category'  :   'Backward Compatability Tests',
    'test'      :   'INVITE With RFC 2543 Syntax Support',
    'id'        :   'inv2543'
}

def inv2543():
    '''
    INVITE With RFC 2543 Syntax Support

    This is a legal message per RFC 2543 (and several bis versions) that
    should be accepted by RFC 3261 elements that want to maintain
    backwards compatibility.
    '''
    log = logging.getLogger('inv2543')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Remove branch parameter from Via
    head['Via'] = rmallParam(head['Via'])
    # Tweak 2: Remove from tag
    head['From'] = rmspcParam(head['From'], 
        param='tag').replace('>', '') + ';user=phone>'
    # Tweak 3: Remove the following headers
    rmhead = (  'Allow', 
                'Contact', 
                'Max-Forwards', 
                'Content-Length'
        )
    for x in rmhead:
        head.pop(x, None)
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg

def run(sock):
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(sock, inv2543(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
