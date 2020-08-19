#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random

def genComb(lst, LW_CONST=3, UP_CONST=7):
    '''
    Takes in a list and generates combination of those chars to form a string
    '''
    # Generating random combinations
    s = ""
    for _ in range(random.randint(LW_CONST, UP_CONST)):
        s += random.choice(lst)
    return s