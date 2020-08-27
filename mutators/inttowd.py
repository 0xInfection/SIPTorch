#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging, math

def inttowd(num: int):
    '''
    Convert integer numbers to words
    '''
    log = logging.getLogger('inttowd')
    if not num:
        log.error('Nothing available for parsing')
        return
    number = int(num)
    number_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    teen_list = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    decades_list = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if number <= 9:
        return(number_list[number].capitalize())
    elif number >= 10 and number <= 19:
        tens = number % 10
        return(teen_list[tens].capitalize())
    elif number > 19 and number <= 99:
        ones = math.floor(number/10)
        twos = ones - 2
        tens = number % 10
        if tens == 0:
            return(decades_list[twos].capitalize())
        elif tens != 0:
            return(decades_list[twos].capitalize() + " " + number_list[tens])
