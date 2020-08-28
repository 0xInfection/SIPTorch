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
from core.utils import parseMsg, catMetHead

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Request Scalar Fields with Overlarge Values',
    'id'        :   'reqsclarg'
}

def reqsclarg():
    '''
    Request Scalar Fields with Overlarge Values

    An element receiving this request should respond with a 400 Bad
    Request due to the CSeq error.  If only the Max-Forwards field were
    in error, the element could choose to process the request as if the
    field were absent.  If only the expiry values were in error, the
    element could treat them as if they contained the default values for
    expiration (3600 in this case).

    Other scalar request fields that may contain aberrant values include,
    but are not limited to, the Contact q value, the Timestamp value, and
    the Via ttl parameter. (Not implemented, maybe later).
    '''
    log = logging.getLogger('reqsclarg')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('REGISTER')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the max-forwards header
    head['Max-Forwards'] = '300'
    # Tweak 2: Add large scalar value in cseq
    head['CSeq'] = head.get('CSeq').replace(
        head.get('CSeq').split(' ')[0], str(random.getrandbits(100)))
    # Tweak 3: Add Expires value > 2**32-1
    head['Expires'] = '1'*100
    # Tweak 4: Contact header expires header
    head['Contact'] += ';expires=%s' % random.getrandbits(100)
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(reqsclarg(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
