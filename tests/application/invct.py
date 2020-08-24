#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, random
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
    '''
    log = logging.getLogger('invct')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the content type
    head['Content-Type'] = 'application/%s' % genRandStr(10)
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg
