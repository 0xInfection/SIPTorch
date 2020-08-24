#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from core.config import IP, RPORT
from core.requester import buildreq
from core.utils import parseMsg, catMetHead

module_info = {
    'category'  :   'Application Layer Semantics',
    'test'      :   'Request-URI with Known but Atypical Scheme',
    'id'        :   'novelscm'
}

def novelscm():
    '''
    OPTIONS Request-URI with Known but Atypical Scheme
    '''
    log = logging.getLogger('novelscm')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('OPTIONS')
    mline, head, body = parseMsg(msg)
    requri = 'beep.boop://%s:%s' % (IP, RPORT)
    # Tweak 1: Remove the following required headers
    mline = mline.replace(mline.split(' ')[1], requri)
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg
