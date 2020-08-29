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
from libs.data import NULL_CHAR
from core.requester.parser import parseMsg, catMetHead

module_info = {
    'category'  :   'Syntactical Parser Tests',
    'test'      :   'Escaped Nulls in URIs',
    'id'        :   'escnull'
}

def escnull():
    '''
    Escaped Nulls in URIs

    This register request contains several URIs with nulls in the
    userpart.  The message is well formed - parsers must accept this
    message.  Implementations must take special care when unescaping the
    Address-of-Record (AOR) in this request so as to not prematurely
    shorten the username.  This request registers two distinct contact
    URIs.
    '''
    log = logging.getLogger('escnull')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('REGISTER')
    mline, head, body = parseMsg(msg)
    # Tweak 1: modify to and from headers
    head['To'] = re.sub(r'sip:\w+?@', 
        'sip:null-%s-null@' % NULL_CHAR, head.get('To'))
    head['From'] = re.sub(r'sip:\w+?@', 
        'sip:null-%s-null@' % NULL_CHAR, head.get('From'))
    # Tweak 2: Modify the contact header
    head['Contact'] = re.sub(r'sip:\w+?@', 
        'sip:%s@' % NULL_CHAR, head.get('Contact'))
    head['CONTACT'] = re.sub(r'sip:\w+?@', 
        'sip:%s@' % (NULL_CHAR*5), head.get('Contact'))
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(escnull(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
