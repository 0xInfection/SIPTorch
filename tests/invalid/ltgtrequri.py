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
    'test'      :   '</> Enclosing Request-URI',
    'id'        :   'ltgtrequri'
}

def ltgtrequri():
    '''
    </> Enclosing Request-URI

    This INVITE request is invalid because the Request-URI has been
    enclosed within in "<>".

    It is reasonable always to reject a request with this error with a
    400 Bad Request.  Elements attempting to be liberal with what they
    accept may choose to ignore the brackets.  If the element forwards
    the request, it must not include the brackets in the messages it
    sends.
    '''
    log = logging.getLogger('ltgtrequri')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Enclose the Req URI within </>
    newuri = '<%s>' % mline.split(' ')[1]
    mline = mline.replace(mline.split(' ')[1], newuri)
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run(sock):
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(sock, ltgtrequri()):
        log.info('Module %s completed' % module_info['test'])
