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
from collections import defaultdict

def makeRequest(method, fromaddr, toaddr, dsthost, cseq=1,
                localtag=None, contentlength=None, contenttype=None):
    """
    Build up the SIP request properly
    method - OPTIONS / INVITE etc
    toaddr = to address
    dsthost = destination host
    callid = callerid
    srchost = source host
    """
    headers = DEF_HSET
    localport = LPORT
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
    srchost = socket.gethostbyname(socket.gethostname())
    headers['Via'] = 'SIP/2.0/UDP %s:%s;branch=z9hG4bK-%s;rport' % (srchost, localport, branchunique)
    headers['Max-Forwards'] = 70
    headers['To'] = toaddr
    headers['From'] = fromaddr
    if localtag is not None:
        headers['From'] += ';tag=%s' % localtag.decode('utf-8')
    if not STATIC_CID:
        headers["Call-ID"] = random.getrandbits(32)
    headers['CSeq'] = '%s %s' % (cseq, method)
    headers['Content-Length'] = len(body)
    if contenttype is None and len(body) > 0:
        contenttype = 'application/sdp'
    if contenttype is not None:
        headers['Content-Type'] = contenttype
    r = '%s %s SIP/2.0\r\n' % (method, uri)
    x = catMetHead(r, headers, body=body)
    return x

if __name__ == "__main__":
    print(makeRequest('INVITE', 'sip:1000@192.168.4.4', 'sip:1@192.13.3.3', '1.1.1.1'))