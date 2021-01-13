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

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Spaces Within Address Specification',
    'id'        :   'spacaddr'
}

def spacaddr():
    '''
    Spaces within address specification

    This request is malformed, since the addr-spec in the To header field
    contains spaces.  Parsers receiving this request must not break.  It
    is reasonable to reject this request with a 400 Bad Request response.
    Elements attempting to be liberal may ignore the spaces.
    '''
    log = logging.getLogger('spacaddr')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseSIPMessage(msg)
    # Tweak 1: add spaces around the To header URL, as simple as that ;)
    head['To'] = head['To'].replace('<', '< ').replace('>', ' >')
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(spacaddr(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
