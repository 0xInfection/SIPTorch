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
    'test'      :   'Unknown Request URI with Unknown Scheme in Header Fields',
    'id'        :   'unkscm2'
}

def unkscm2():
    '''
    Unknown Request URI with Unknown Scheme in Header Fields
    '''
    log = logging.getLogger('unkscm2')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('REGISTER')
    mline, head, body = parseMsg(msg)
    # Tweak 1: modify the header URI scheme
    head['To'] = '%s:%s' % (genRandStr(4), random.getrandbits(32))
    fromhead = head['From']
    head['From'] = fromhead.replace(fromhead.split(';')[0], '<http://example.com>')
    head['Contact'] = '<name:siptorch_flames>'
    # Forming the request message back up
    mg = catMetHead(mline, head, body=body)
    return mg
