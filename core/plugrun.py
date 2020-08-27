#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import os
import socket
import logging
import pluginbase
from core import config
from core.logger import logresp
from core.requester import connector

def runPlugin(sock, msg: str, minfo: dict):
    '''
    Perform the request and print results
    '''
    log = logging.getLogger('plugrun')
    if not (sock or msg):
        log.critical('Nothing received as request body')
        return
    log.debug("Sending the request")
    try:
        connector.sendreq(sock, msg)
        data, *_ = connector.handler(sock)
        log.debug('\nRequest: %s\nResponse: %s' % (msg, data))
        log.debug('Logging data to file')
        logdata = '''
### Test: %s
- Category: %s
- ID: `%s`
- Request:
```
%s
```
- Response:
```
%s
```

        ''' % (minfo['test'], minfo['category'], minfo['id'], msg, data)
        logresp(logdata)
        return True
    except socket.error as err:
        log.critical('Something\'s not right here: %s' % err.__str__())
        return 

def runAll(sock):
    '''
    Runs all the plugins at once
    '''
    plugin = pluginbase.PluginBase(package='tests')
    pluginsource = plugin.make_plugin_source(
        searchpath=['./tests/application', 
                    './tests/backcomp', 
                    './tests/invalid',
                    #'./tests/parser',
                    './tests/transaction'
                ])
    for plug in pluginsource.list_plugins():
        p = pluginsource.load_plugin(plug)
        p.run(sock)