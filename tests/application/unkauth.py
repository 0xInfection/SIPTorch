#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, random
from core.requester import buildreq
from core.plugrun import runPlugin
from core.utils import parseMsg, catMetHead
from mutators.replparam import genRandStr

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'Unknown/Invalid Authorization Scheme',
    'id'        :   'unkauth'
}

def unkauth():
    '''
    Unknown/Invalid Authorization Scheme

    The request is well formed.  A parser must not fail
    when receiving it.

    A proxy will treat this request as it would any other REGISTER. If
    it forwards the request, it will include this Authorization header
    field unmodified in the forwarded messages.

    A registrar that does not care about challenge-response
    authentication will simply ignore the Authorization header field,
    processing this registration as if the field were not present. A
    registrar that does care about challenge-response authentication will
    reject this request with a 401, issuing a new challenge with a scheme
    it understands.

    Endpoints choosing not to act as registrars will simply reject the
    request. A 405 Method Not Allowed is appropriate.
    '''
    log = logging.getLogger('unkauth')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('REGISTER')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Add invalid auth scheme
    head['Authorization'] = '%s %s' % (genRandStr, 'randparam-data=valuehere')
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(unkauth(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
