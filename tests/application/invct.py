#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from core.requester import buildreq
from core.utils import parseMsg, catMetHead
from mutators.replparam import genRandStr

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'Unknown/Invalid Content Type',
    'id'        :   'invct'
}

def invct():
    '''
    Unknown/Invalid Content Type

    This INVITE request contains a body of unknown type.  It is
    syntactically valid.  A parser must not fail when receiving it.

    A proxy receiving this request would process it just as it would any
    other INVITE.  An endpoint receiving this request would reject it
    with a 415 Unsupported Media Type error.
    '''
    log = logging.getLogger('invct')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the content type
    head['Content-Type'] = 'application/%s' % genRandStr(10)
    # Tweak 2: Modify the body
    body = '<audio>\r\n  <pcmu port="443"/>\r\n</audio>'
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg
