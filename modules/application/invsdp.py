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
from mutators.replparam import genRandStr

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'Invalid/Unacceptable Accept Offering',
    'id'        :   'invsdp'
}

def invsdp():
    '''
    Invalid/Unacceptable Accept Offering

    This request indicates that the response must contain a body in an
    unknown type.  In particular, since the Accept header field does not
    contain application/sdp, the response may not contain an SDP body.
    The recipient of this request could respond with a 406 Not
    Acceptable, with a Warning/399 indicating that a response cannot be
    formulated in the formats offered in the Accept header field.  
    
    It is also appropriate to respond with a 400 Bad Request, since all 
    SIP User-Agents (UAs) supporting INVITE are required to support
    application/sdp.
    '''
    log = logging.getLogger('invsdp')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('REGISTER')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Invalid Accept offering
    head['Accept'] = 'text/%s' % genRandStr(7)
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(invsdp(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
