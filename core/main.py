#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import time
import socket
import logging
from core import config
from core.plugrun import runAll
from core.utils import validateHost
from core.requester import connector
from core.logger import loggerinit, logfooter

def startEngine():
    '''
    The main stuff
    '''
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('main')
    timestart = time.time()
    log.info('Testing target')
    ip = validateHost(config.RHOST)
    config.IP = ip
    if not ip:
        log.critical("Invalid target specified, please check your input URL")
    log.debug('Initiating socket connection')
    loggerinit()
    runAll()
    log.info('All modules completed.')
    timeend = time.time()
    log.info('Total time taken: %.3fs' % (timeend - timestart))
    logfooter(timestart, timeend)
