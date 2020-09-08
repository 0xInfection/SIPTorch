#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from core.plugrun import runPlugin
from core.requester import buildreq
from core.requester.parser import parseMsg, catMetHead

module_info = {
    'category'  :   'Syntactical Parser Tests',
    'test'      :   'Unusual Reason Phrase',
    'id'        :   'unreason'
}

def unreason():
    '''
    Unusual Reason Phrase

    This 200 response contains a reason phrase other than "OK".  The
    reason phrase is intended for human consumption and may contain any
    string produced by

        Reason-Phrase   =  *(reserved / unreserved / escaped
                            / UTF8-NONASCII / UTF8-CONT / SP / HTAB)

    This particular response contains unreserved and non-ascii UTF-8
    characters.  This response is well formed.  A parser must accept this
    message.
    '''
    log = logging.getLogger('unreason')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the header of the message
    # We are using a 20 char to form the remaining
    utfencstr = r'e0a6a4e0a6ace0a78720e0a68fe0a695e0a6b6e0a'
    utfencstr += r'78b20e0a6a8e0a6bfe0a6b0e0a6bee0a6a8e0a6ace0a78de'
    utfencstr += r'0a6ace0a68720e0a6afe0a6a5e0a787e0a6b7e0a78de0a'
    utfencstr += r'69f20e0a6b8e0a6b9e0a69c20e0a69be0a6bfe0a6b2'
    mline = 'SIP/2.0 200 = %s * %s %s' % ('2**5', '5**2',
        bytearray.fromhex(utfencstr).decode('utf-8'))
    # Forming the message up back again
    mg = catMetHead(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(unreason(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
