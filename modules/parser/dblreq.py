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
    'test'      :   'Extra Trailing Octets in a UDP Datagram',
    'id'        :   'dblreq'
}

def dblreq():
    '''
    Extra Trailing Octets in a UDP Datagram

    This message contains a single SIP REGISTER request, which ostensibly
    arrived over UDP in a single datagram.  The packet contains extra
    octets after the body (which in this case has zero length).  The
    extra octets happen to look like a SIP INVITE request, but (per
    section 18.3 of [RFC3261]) they are just spurious noise that must be
    ignored.

    A SIP element receiving this datagram would handle the REGISTER
    request normally and ignore the extra bits that look like an INVITE
    request.  If the element is a proxy choosing to forward the REGISTER,
    the INVITE octets would not appear in the forwarded request.
    '''
    log = logging.getLogger('dblreq')
    log.info('Testing module: %s' % module_info['test'])
    msg1 = buildreq.makeRequest('REGISTER')
    msg2 = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg1)
    # Tweak 1: Add the body of msg1 as msg2, short hack
    body = '\r\n%s' % msg2
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(dblreq(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
