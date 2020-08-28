#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, random
from core.plugrun import runPlugin
from core.requester import buildreq
from mutators.inttowd import inttowd
from core.utils import parseMsg, catMetHead

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Negative Content-Length',
    'id'        :   'intwdcl'
}

def intwdcl():
    '''
    Negative Content-Length

    This request has a negative value for Content-Length.

    An element receiving this message should respond with an error.  This
    request appeared over UDP, so the remainder of the datagram can
    simply be discarded.
    '''
    log = logging.getLogger('intwdcl')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the content length header
    if int(head.get('Content-Length')) > 99:
        head['Content-Length'] = inttowd(99)
    else:
        head['Content-Length'] = inttowd(head.get('Content-Length'))
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(intwdcl(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
