#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, datetime
from core.plugrun import runPlugin
from core.requester import buildreq
from core.utils import parseMsg, catMetHead

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Invalid Time Zone in Date Header Field',
    'id'        :   'baddate'
}

def baddate():
    '''
    Invalid Time Zone in Date Header Field

    This INVITE is invalid, as it contains a non-GMT time zone in the SIP
    Date header field.

    It is acceptable to reject this request as malformed (though an
    element shouldn't do that unless the contents of the Date header
    field were actually important to its processing).  An element wishing
    to be liberal in what it accepts could ignore this value altogether
    if it wasn't going to use the Date header field anyway.  Otherwise,
    it could attempt to interpret this date and adjust it to GMT.

    RFC 3261 explicitly defines the only acceptable time zone designation
    as "GMT".  "UT", while synonymous with GMT per RFC 2822, is not
    valid.  "UTC" and "UCT" are also invalid.
    '''
    log = logging.getLogger('baddate')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    x = datetime.datetime.now()
    # Tweak 1: Add non-GMT timezone to date header
    head['Date'] = '%s, %s %s %s %s EST' % (x.strftime('%a'), x.strftime('%d'),
        x.strftime('%b'), x.strftime('%Y'), x.strftime('%X'))
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(baddate(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
