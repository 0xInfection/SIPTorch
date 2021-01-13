#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from libs import config
from core.plugrun import runPlugin
from core.requester import buildreq
from core.requester.parser import parseSIPMessage, concatMethodxHeaders
from mutators.replparam import genRandStr

module_info = {
    'category'  :   'Syntactical Parser Tests',
    'test'      :   'Multipart MIME Message',
    'id'        :   'mpmime'
}

def mpmime():
    '''
    Multipart MIME Message

    This MESSAGE request contains two body parts. The second part is
    binary encoded and contains null (0x00) characters. Receivers must
    take care to frame the received message properly.

    Parsers must accept this message as well formed, even if the
    application above the parser does not support multipart/signed.

    Additional examples of multipart/mime messages, in particular S/MIME
    messages, are available in the security call flow examples document.
    '''
    log = logging.getLogger('mpmime')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('MESSAGE')
    mline, head, body = parseSIPMessage(msg)
    # Message to be sent over
    cer = r'3082015206092A864886F70D010702A08201433082013F02'
    cer += r'01013109300706052B0E03021A300B06092A864886F70D010701318201203082'
    cer += r'011C020101307C3070310B300906035504061302555331133011060355040813'
    cer += r'0A43616C69666F726E69613111300F0603550407130853616E204A6F7365310E'
    cer += r'300C060355040A1305736970697431293027060355040B132053697069742054'
    cer += r'65737420436572746966696361746520417574686F7269747902080195007102'
    cer += r'330113300706052B0E03021A300D06092A864886F70D01010105000481808EF4'
    cer += r'66F948F0522DD2E5978E9D95AAE9F2FE15A06659716292E8DA2AA8D8350A68CE'
    cer += r'FFAE3CBD2BFF1675DDD5648E593DD64728F26220F7E941749E330D9A15EDABDB'
    cer += r'93D10C42102E7B7289D29CC0C9AE2EFBC7C0CFF9172F3B027E4FC027E1546DE4'
    cer += r'B6AA3ABB3E66CCCB5DD6C64B8383149CB8E6FF182D944FE57B65BC99D005'
    # Boundary to be used
    boundary = genRandStr(16, allow_digits=True)
    # Tweak 1: Add a route header
    head['Route'] = '<sip:127.0.0.1:5080>'
    # Tweak 2; Add the identity header
    head['Identity'] = config.IDENTITY
    # Tweak 3: Add cte header to binary
    head['Content-Transfer-Encoding'] = 'binary'
    # Tweak 4: Add multipart/mixed to content type
    head['Content-Type'] = 'multipart/mixed;boundary=%s' % boundary
    # Tweak 5: Add the body
    body = '--%s\r\nContent-Type: text/plain\r\nContent-Transfer-Encoding' % boundary
    body += ': binary\r\n\r\nHi from siptorch - pls dont break\r\n--%s\r\n' % boundary
    body += 'Content-Type: application/octet-stream\r\nContent-Tran'
    body += 'sfer-Encoding: binary\r\n\r\n%s\r\n--%s--' % (
        bytearray.fromhex(cer).decode('utf-8', errors='ignore'), boundary)
    # Tweak 6: Add content-length header
    head['Content-Length'] = len(body)
    # Forming the message up back again
    mg = concatMethodxHeaders(mline, head, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(mpmime(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
