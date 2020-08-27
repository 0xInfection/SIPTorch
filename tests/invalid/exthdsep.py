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
from core.utils import parseMsg, catMetHead

module_info = {
    'category'  :   'Invalid Messages',
    'test'      :   'Extraneous Header Field Separators',
    'id'        :   'exthdsep'
}

def exthdsep():
    '''
    Extraneous Header Field Separators

    The Via header field of this request contains additional semicolons
    and commas without parameters or values.  The Contact header field
    contains additional semicolons without parameters.  This message is
    syntactically invalid.

    An element receiving this request should respond with a 400 Bad
    Request error.
    '''
    log = logging.getLogger('exthdsep')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Modify the via header
    head['Via'] += r';;,;,,'
    # Tweak 2: Add contact header
    head['Contact'] += r';;;;,;'
    mg = catMetHead(mline, head, body=body)
    return mg

def run(sock):
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(sock, exthdsep()):
        log.info('Module %s completed' % module_info['test'])
