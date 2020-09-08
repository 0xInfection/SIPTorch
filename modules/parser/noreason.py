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
from core.requester.parser import parseMsg, catMetHead

module_info = {
    'category'  :   'Syntactical Parser Tests',
    'test'      :   'Content Length Larger Than Message',
    'id'        :   'noreason'
}

def noreason():
    '''
    Empty Reason Phrase

    This well-formed response contains no reason phrase.  A parser must
    accept this message.  The space character after the reason code is
    required.  If it were not present, this message could be rejected as
    invalid (a liberal receiver would accept it anyway).
    '''
    log = logging.getLogger('noreason')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the header of the message
    # We are using a \x20 char to form the remaining 
    mline = 'SIP/2.0 100%s' % bytearray.fromhex('20').decode('utf-8')
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(noreason(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
