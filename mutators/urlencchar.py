#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
import random
from libs.data import URL_MAP

def urlEncodeStr(st: str, randomchoice=True, value=3):
    '''
    Add random headers to the default header set
    st: string to process
    randomchoice: whether to randomly encode or not
    value: how many chars to encode/change
    '''
    wordlist = list(st)
    if randomchoice:
        ksample = random.sample(range(0, len(st)), value)
        for ind in ksample:
            wordlist[ind] = URL_MAP[wordlist[ind]]
    else:
        for x in range(len(wordlist)):
            wordlist[x] = URL_MAP[wordlist[x]]
    # Join up now
    return ''.join(wordlist)

def urlEncodeChar(ch: str):
    '''
    URL Encode a char passed to the function
    '''
    return URL_MAP[ch]
