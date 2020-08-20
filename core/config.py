#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

# This file contains all core config variables to be used 
# during the SIP torture tests

USER_AGENT = 'siptorch/0.1'

# TO be implemented later
IP6_SUPPORT = False

# Request method to test. If this var is set to "all" then all existing
# tests will be done, otherwise specify your method explicitly
# METHOD = "INVITE" 
METHOD = 'all'

# Default extension to test against
DEF_EXT = "1000"

# Local port to use
LPORT = 5060

# Extra headers to add to the default header set
EXT_HEADERS = {
    'UnknownHeaderWithUnusualValue': ';;,,;;,;',
    'NewFangledHeader': '''   newfangled value\r\ncontinued newfangled value''',
}