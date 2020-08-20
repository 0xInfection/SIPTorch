#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random
from core.config import *
from collections import defaultdict

def makeRequest(method, fromaddr, toaddr, dsthost, port, callid, srchost='', branchunique=None, cseq=1,
    auth=None, localtag=None, compact=False, contact='sip:123@1.1.1.1', accept='application/sdp', contentlength=None,
    contenttype=None, body='', requesturi=None):
    """makeRequest builds up a SIP request
    method - OPTIONS / INVITE etc
    toaddr = to address
    dsthost = destination host
    port = destination port
    callid = callerid
    srchost = source host
    """
    useragent = USER_AGENT
    localport = LPORT
    extension = DEF_EXT
    if extension is None or method == 'REGISTER':
        uri = 'sip:%s' % dsthost
    else:
        uri = 'sip:%s@%s' % (extension, dsthost)
    if branchunique is None:
        branchunique = '%s' % random.getrandbits(32)
    headers = defaultdict()
    finalheaders = defaultdict()
    superheaders = defaultdict()
    if method == 'ACK':
        localtag = None
    if compact:
        superheaders[
            'v'] = 'SIP/2.0/UDP %s:%s;branch=z9hG4bK-%s;rport' % (srchost, port, branchunique)
        headers['t'] = toaddr
        headers['f'] = fromaddr
        if localtag is not None:
            headers['f'] += ';tag=%s' % localtag.decode('utf-8')
        headers['i'] = callid
        # if contact is not None:
        headers['m'] = contact
    else:
        superheaders[
            'Via'] = 'SIP/2.0/UDP %s:%s;branch=z9hG4bK-%s;rport' % (srchost, localport, branchunique)
        headers['Max-Forwards'] = 70
        headers['To'] = toaddr
        headers['From'] = fromaddr
        headers['User-Agent'] = useragent
        if localtag is not None:
            headers['From'] += ';tag=%s' % localtag.decode('utf-8')
        headers['Call-ID'] = callid
        # if contact is not None:
        headers['Contact'] = contact
    headers['CSeq'] = '%s %s' % (cseq, method)
    headers['Max-Forwards'] = 70
    headers['Accept'] = accept
    if contentlength is None:
        headers['Content-Length'] = len(body)
    else:
        headers['Content-Length'] = contentlength
    if contenttype is None and len(body) > 0:
        contenttype = 'application/sdp'
    if contenttype is not None:
        headers['Content-Type'] = contenttype

    r = '%s %s SIP/2.0\r\n' % (method, uri)
    if requesturi is not None:
        r = '%s %s SIP/2.0\r\n' % (method, requesturi)
    for h in superheaders.items():
        r += '%s: %s\r\n' % h
    for h in headers.items():
        r += '%s: %s\r\n' % h
    for h in finalheaders.items():
        r += '%s: %s\r\n' % h
    r += '\r\n'
    r += body
    return(r)
