#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, random
from libs import config
from core.plugrun import runPlugin
from core.requester import buildreq
from core.requester.parser import parseSIPMessage, concatMethodxHeaders

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'Multiple Values in Single Value Required Fields',
    'id'        :   'multireq'
}

def multireq():
    '''
    Multiple Values in Single Value Required Fields

    An element receiving this request would respond with a 400 Bad
    Request error.
    '''
    log = logging.getLogger('multireq')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseSIPMessage(msg)
    # Tweak 1: Add multiple keys with same value duplicate
    # The RFC 3261 says that the SIP message is not case-sensitive
    # So what we do to exploit this is, lowercase the keys to form 
    # duplicates, since in no way a dict can hold duplicates
    #
    # Duplicating the following fields - call-id, to, from, max-
    # forwards, cseq headers
    head['call-id'] = random.getrandbits(80)
    head['cseq'] = '600 INVITE'
    head['to'] = 'sip:6969@%s' % config.RHOST
    head['from'] = 'sip:2020@%s;tag=%s' % (config.RHOST, random.getrandbits(32))
    head['max-forwards'] = '5'
    # Recompiling our message
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(multireq(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
