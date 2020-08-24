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
    'test'      :   'Unknown/Invalid Authorization Scheme',
    'id'        :   'unkauth'
}

def unkauth():
    '''
    Unknown/Invalid Authorization Scheme
    '''
    log = logging.getLogger('unkauth')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('REGISTER')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Add invalid auth scheme
    head['Authorization'] = '%s %s' % (genRandStr, 'randparam-data=valuehere')
    mg = catMetHead(mline, head, body=body)
    return mg
