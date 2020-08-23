#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random, socket
from core.config import *
from core.utils import catMetHead

def makeRequest(method, dsthost, contentlength=None, contenttype=None):
    """
    Build up the SIP request properly
    method - OPTIONS / INVITE etc
    toaddr = to address
    dsthost = destination host
    callid = callerid
    srchost = source host
    """
    headers = DEF_HSET
    extension = DEF_EXT
    branchunique = BRANCH
    if 'invite' in method.lower():
        body = INVITE_BODY
    else: body = ''
    if extension is None or method == 'REGISTER':
        uri = 'sip:%s' % dsthost
    else:
        uri = 'sip:%s@%s' % (extension, dsthost)
    if branchunique is None:
        branchunique = '%s' % random.getrandbits(32)
    if method == 'ACK':
        localtag = None
    if not SRC_HOST:
        srchost = socket.gethostbyname(socket.gethostname())
    else: srchost = SRC_HOST
    headers['Via'] = 'SIP/2.0/UDP %s:%s;branch=z9hG4bK-%s;rport' % (srchost, LPORT, branchunique)
    headers['Max-Forwards'] = 70
    headers['To'] = TO_ADDR
    headers['From'] = FROM_ADDR
    if FROM_TAG is None:
        headers['From'] += ';tag='+str(random.getrandbits(90))
    else: headers['From'] += ';tag='+FROM_TAG
    if not STATIC_CID:
        headers["Call-ID"] = random.getrandbits(80)
    headers['CSeq'] = '%s %s' % (CSEQ, method)
    headers['Content-Length'] = len(body)
    if 'register' not in method.lower():
        headers['Contact'] = 'sip:%s@%s:%s' % (DEF_EXT, srchost, LPORT)
    if contenttype is None and len(body) > 0:
        contenttype = 'application/sdp'
    if contenttype is not None:
        headers['Content-Type'] = contenttype
    r = '%s %s SIP/2.0\r\n' % (method, uri)
    x = catMetHead(r, headers, body=body)
    return x

if __name__ == "__main__":
    print(makeRequest('INVITE', 'sip:1000@192.168.4.4', 'sip:1@192.13.3.3', '1.1.1.1'))