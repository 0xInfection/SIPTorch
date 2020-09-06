#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

from libs import config
import logging, socket, random
from core.plugrun import runPlugin
from core.requester import buildreq
from core.requester.parser import parseMsg, catMetHead

module_info = {
    'category'  :   'Syntactical Parser Tests',
    'test'      :   'Varied and Unknown Transport Types',
    'id'        :   'transports'
}

def transports():
    '''
    Varied and Unknown Transport Types

    This request contains Via header field values with all known
    transport types and exercises the transport extension mechanism.
    Parsers must accept this message as well formed.  Elements receiving
    this message would process it exactly as if the 2nd and subsequent
    header field values specified UDP (or other transport).
    '''
    log = logging.getLogger('transports')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Add multiple via headers
    # So here's a hurdle, what happens here is that python dict doesn't
    # allow duplicate dicts, so we permutate the letters toggling upper/
    # lowercase to form different headers, since headers are 
    # case-insensitive as mentioned in the RFC
    srchost = socket.gethostbyname(
        socket.gethostname()) if not config.SRC_HOST else config.SRC_HOST
    # Add udp as transport method in via header
    head['via'] = 'SIP/2.0/TCP %s:%s;branch=z9hG4bK-%s;rport' % \
        (srchost, config.LPORT, random.getrandbits(32))
    # Add unknown type as transport method in via header
    head['VIa'] = 'SIP/2.0/UNKNOWN %s:%s;branch=z9hG4bK-%s;rport' % \
        (srchost, config.LPORT, random.getrandbits(32))
    # Add tls as transport method in via header
    head['vIA'] = 'SIP/2.0/TLS %s:%s;branch=z9hG4bK-%s;rport' % \
        (srchost, config.LPORT, random.getrandbits(32))
    # Add sctp as transport method in via header
    head['vIa'] = 'SIP/2.0/SCTP %s:%s;branch=z9hG4bK-%s;rport' % \
        (srchost, config.LPORT, random.getrandbits(32))
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(transports(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
