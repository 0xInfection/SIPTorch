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
from core.requester.parser import parseSIPMessage, concatMethodxHeaders
from mutators.replparam import rmallParam, rmspcParam

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Request Method with CSeq Method Mismatch',
    'id'        :   'cseqmatch'
}

def cseqmatch():
    '''
    Request Method with CSeq Method Mismatch

    This request has mismatching values for the method in the start line
    and the CSeq header field.  Any element receiving this request will
    respond with a 400 Bad Request.
    '''
    log = logging.getLogger('cseqmatch')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseSIPMessage(msg)
    # Tweak 1: Modify CSeq header
    head['CSeq'] = '5 INVITE'
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(cseqmatch(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
