#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
import random, socket
from libs.config import *
from core.utils import validateHost
from core.requester.parser import catMetHead
from mutators.replparam import genRandStr

def makeRequest(method, bsbody='', contentlength=None):
    '''
    Build up the SIP request properly from scratch
    '''
    headers = DEF_HSET
    extension = DEF_EXT
    branch = BRANCH
    body = ''
    if not SRC_HOST:
        srchost = socket.gethostbyname(socket.gethostname())
    dsthost = IP  # if IP else validateHost(RHOST)
    if 'invite' in method.lower():
        body = INVITE_BODY
        body = body.replace('x.x.x.x', srchost).replace('y.y.y.y', dsthost)
    if bsbody: 
        body = bsbody
    if extension is None or method.upper() == 'REGISTER':
        uri = 'sip:%s' % dsthost
    else:
        uri = 'sip:%s@%s' % (extension, dsthost)
    if not BRANCH:
        branch = '%s' % random.getrandbits(32)
    else: srchost = SRC_HOST
    headers['Via'] = 'SIP/2.0/UDP %s:%s;branch=z9hG4bK-%s;rport' % (srchost, LPORT, branch)
    headers['Max-Forwards'] = 70
    if not (TO_ADDR or FROM_ADDR):
        senderext = genRandStr(5)
        headers['To'] = '"%s" <sip:%s@%s>' % (DEF_EXT, DEF_EXT, RHOST)
        headers['From'] = '"siptorch" <sip:%s@%s>' % (senderext, RHOST)
    # If method is register, we need to modify To, From header fields
    if method == 'REGISTER':
        headers['From'] = '"%s" <sip:%s@%s>' % (extension, extension, RHOST)
        headers['To'] = headers['From']
    if method.lower() != 'ack':
        if FROM_TAG is None:
            headers['From'] += ';tag='+str(random.getrandbits(90))
        else: headers['From'] += ';tag='+FROM_TAG
    if not STATIC_CID:
        headers["Call-ID"] = random.getrandbits(80)
    headers['CSeq'] = '%s %s' % (CSEQ, method)
    headers['Content-Length'] = len(body)
    if 'register' not in method.lower():
        headers['Contact'] = '<sip:%s@%s>' % (senderext, RHOST)
    if CONTENT_TYPE is None and len(body) > 0:
        contenttype = 'application/sdp'
    else: contenttype = CONTENT_TYPE
    if contenttype is not None:
        headers['Content-Type'] = contenttype
    r = '%s %s SIP/2.0\r\n' % (method, uri)
    x = catMetHead(r, headers, body=body)
    return x
