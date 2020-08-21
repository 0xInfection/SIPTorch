#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import socket, logging
from core.utils import parseMsg 

def parseResponse(buff, addr):
    '''
    Figuring out the SIP response
    '''
    log = logging.getLogger("parseResponse")
    if not (buff or addr):
        log.error("Nothing available for parsing")
        return
    ip, port, *_ = addr
    # Decoding the buffer in response
    data = buff.decode('utf-8', 'ignore')
    return (data, ip, port)

