#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import random
from libs.chars import NULL_CHAR

# Upper costraint
UP_CONST = 7
# Lower constraint
LW_CONST = 3

def nullInsert(msg: str, lent=1):
    '''
    Inserts random null chars into strings randomly.
    '''
    chard = NULL_CHAR * lent
    return ''.join('%s%s' % (x, random.choice((chard, ""))) for x in msg)

if __name__ == "__main__":
    print(nullInsert('aaaaaaaaaaa', lent=2))