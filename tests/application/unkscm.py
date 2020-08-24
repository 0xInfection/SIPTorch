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

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'OPTIONS Request URI with Unknown Scheme',
    'id'        :   'unkscm'
}

def unkscm():
    log = logging.getLogger('unkscm')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseMsg(msg)
    # Tweak 1: modify the request URI scheme
    mline = mline.replace(mline.split(' ')[1], 'unknownscheme:unknowncontent')
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg
