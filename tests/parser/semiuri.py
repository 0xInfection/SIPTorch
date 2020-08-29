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
    'test'      :   'Semicolon-Separated Parameters in URI User Part',
    'id'        :   'semiuri'
}

def semiuri():
    '''
    Semicolon-Separated Parameters in URI User Part

    This request has a semicolon-separated parameter contained in the
    "user" part of the Request-URI (whose value contains an escaped @
    symbol).  Receiving elements will accept this as a well-formed
    message.  The Request-URI will parse so that the user part is
    "user;par=u@example.net".
    '''
    log = logging.getLogger('semiuri')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the header options uri
    newuri = mline.split(' ')[1] 
    nuri = '%s;param=u%sinfectedsip.net@%s' % (
        newuri.split('@')[0], r'%40', newuri.split('@')[1])
    mline = mline.replace(mline.split(' ')[1], nuri)
    # Tweak 2: Add the Accept header
    head['Accept'] = 'application/sdp, application/pkcs7-mime, '
    head['Accept'] += 'multipart/mixed, multipart/signed, '
    head['Accept'] += 'message/sip, message/sipfrag'
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(semiuri(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
