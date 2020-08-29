#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging

def permuteCase(inp: str): 
    '''
    Generate maximum permutations by changing case
    '''
    log = logging.getLogger('permuteCase')
    if not inp:
        log.error('Nothing available for parsing')
        return
    n = len(inp)
    mx = 1 << n
    inp = inp.lower()
    maxperm = list()
    for i in range(mx): 
        combination = [k for k in inp] 
        for j in range(n): 
            if ((i >> j) & 1) == 1: 
                combination[j] = inp[j].upper() 
        temp = ''
        for i in combination: 
            temp += i 
        maxperm.append(temp)
    return maxperm