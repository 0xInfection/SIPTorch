#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random
from libs import lws
from utils.utils import genComb

# Upper costraint
UP_CONST = 7
# Lower constraint
LW_CONST = 3

def lwsInsert(msg, charc='random'):
    '''
    Inserts random lws characters into strings
    '''
    # Fetching all whitespace chars
    if hasattr(lws, '__all__'):
        wschars = [getattr(lws, name) for name in lws.__all__]
    else:
        wschars = [getattr(lws, name) for name in dir(lws) if not name.startswith('_')]

    # Generate the character sequence
    if charc is 'random':
        return ''.join('%s%s' % (x, random.choice((random.choice(wschars), ""))) for x in msg)
    else:
        return ''.join('%s%s' % (x, random.choice((charc, ""))) for x in msg)
    