#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import logging
from libs import config
from core.plugrun import runPlugin
from core.requester import buildreq
from mutators.multihead import multiHead
from core.requester.parser import parseMsg, catMetHead

module_info = {
    'category'  :   'Syntactical Parser Tests',
    'test'      :   'Long Values in Header Fields',
    'id'        :   'longreq'
}

def longreq():
    '''
    Long Values in Header Fields

    This well-formed request contains header fields with many values and
    values that are very long.
    '''
    log = logging.getLogger('longreq')
    log.info('Testing module: %s' % module_info['test'])
    msg = buildreq.makeRequest('INVITE')
    mline, head, body = parseMsg(msg)
    # Tweak 1: Such long To value
    longto = "I have a user name of %s proportion" % ('extreme'*10)
    head['To'] = "%s <%s" % (longto, head.get('To').split('<')[1])
    head['To'] += ";unknownparam=veryl%sgnvalue" % ('o'*70)
    head['To'] += ";longparam%s=shortvalue" % ('name'*25)
    head['To'] += "very%sparamwithnovalueatall" % ('long'*25)
    # Tweak 2: Such long From Value
    head['From'] = 'sip:%s@%s' % (('soverylongusernameOOF'*5), config.RHOST)
    head['From'] += ';tag=10%s420' % ('789'*50)
    head['From'] += ';unknownheadparam%sname=some%shere' % (
            ('awkwardlylong'*10), ('verylong'*10))
    head['From'] += 'paramless%s' % ('value'*10)
    # Tweak 3: add call id
    head['Call-ID'] = 'longreq.one%slongcallidhere' % ('damnlong'*10)
    # Tweak 4: add contact
    head['Contact'] = '<sip:%s@%s>' % (('toolongtohandle'*10), config.RHOST)
    # Tweak 5: add unknown value
    head['Unknown-L%sng-Field' % ('o'*75)] = '%s;%s=%s' % (
        'unknown-%s-value' % ('long'*20),
        'unknown-%s-parameter-name' % ('long'*20),
        'unknown-%s-parameter-value' % ('long'*20)
    )
    # Tweak 6: multiply the number of via headers
    pset = multiHead('Via', permuteasdict=True, singlestr=False)
    # Merging both the dicts together
    try:
        newhead = { **pset, **head }
    except Exception as e:
        log.error('Action not supported: %s' % e.__str__())
        newhead = pset.copy()
        newhead.update(head)
    sipc = 1
    for x in newhead.keys():
        if not newhead.get(x):
            newhead[x] = 'SIP/2.0/UDP sip%s.infectedsip.com' % sipc
            sipc += 1  # incrementing the value properly
    # Forming the message up back again
    mg = catMetHead(mline, newhead, body=body)
    return mg

def run():
    '''
    Run this module by sending the actual request
    '''
    log = logging.getLogger('run')
    if runPlugin(longreq(), minfo=module_info):
        log.info('Module %s completed' % module_info['test'])
