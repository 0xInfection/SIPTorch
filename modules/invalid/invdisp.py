#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, random
from libs import config
from core.plugrun import runPlugin
from core.requester import buildreq
from core.requester.parser import parseSIPMessage, concatMethodxHeaders
from mutators.replparam import rmallParam, rmspcParam

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Non-token Characters in Display Name',
    'id'        :   'invdisp'
}

def invdisp():
    '''
    Non-token Chars in Display Name

    This OPTIONS request is malformed, since the display names in the To
    and From header fields contain non-token characters but are unquoted.

    It is reasonable always to reject this kind of error with a 400 Bad
    Request response.

    An element may attempt to be liberal in what it receives and infer
    the missing quotes.  If this element were a proxy, it must not
    propagate the error into the request it forwards.  As a consequence,
    if the fields are covered by a signature, there's not much point in
    trying to be liberal - the message should simply be rejected.
    '''
    log = logging.getLogger('invdisp')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseSIPMessage(msg)
    # Tweak 1: Modify add untokenized header display names
    head['From'] = '%s, %s <sip:%s@%s>;tag=%s' % (
        'siptorch', 'testing', config.DEF_EXT, config.RHOST, random.getrandbits(32))
    head['To'] = '%s, %s, %s <sip:%s@%s>' % (
            'server', "shouldn't", 'break', config.DEF_EXT, config.RHOST)
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(invdisp(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
