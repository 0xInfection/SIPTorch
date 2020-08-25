#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import sys
import socket
import logging

# Importing the tests
'''
from tests.parser import ()
from tests.invalid import ()
from tests.backcomp import ()
from tests.application import ()
from tests.transaction import ()
'''
# Requestor modules
from core.requester import (
    buildreq, 
    connector,
    parser
)
from core import config
from tests.backcomp.inv2543 import inv2543
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('main')
log.info('Testing target')
ip = parser.validateHost(config.RHOST)
config.IP = ip
if not ip:
    log.critical("Invalid target specified, please check your input URL")
log.debug('Initiating socket connection')
sock = connector.sockinit()
req = inv2543()
try:
    connector.sendreq(sock, req)
    data, host, port = connector.handler(sock)
    print("Target: \n%s:%s" % (host, port))
    print("\nRequest: \n%s\n" % req)
except socket.error as e:
    log.warn("Something's not right: %s" % e.__str__)
if data:
    print("Response: \n%s" % data)