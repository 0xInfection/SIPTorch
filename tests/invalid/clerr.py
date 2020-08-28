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
    'test'      :   'Content Length Larger Than Message',
    'id'        :   'clerr'
}

def clerr():
    '''
    Content Length Larger Than Message

    This is a request message with a Content Length that is larger than
    the actual length of the body.

    When sent over UDP (as this message ostensibly was), the receiving
    element should respond with a 400 Bad Request error.
    '''
    log = logging.getLogger('clerr')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the content length header
    head['Content-Length'] = '%s' % 9999
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(clerr(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
