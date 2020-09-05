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
from core.options import *
from core.plugrun import runAll
from core.colors import G
from core.utils import calcLogLevel
from core.requester import connector
from core.logger import loggerinit, logfooter, CustomFormatter

def startEngine():
    '''
    The main stuff
    '''
    formatter = CustomFormatter()
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(fmt=formatter)
    logging.root.addHandler(hdlr=handler)
    logging.root.setLevel(level=calcLogLevel(args))
    timestart = time.time()
    loggerinit()
    runAll()
    print(G, 'All modules completed.')
    timeend = time.time()
    print(G, 'Total time taken: %.3fs' % (timeend - timestart))
    logfooter(timestart, timeend)
