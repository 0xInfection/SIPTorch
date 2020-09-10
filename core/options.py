#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

import os, sys
import logging
import argparse
from libs import config
from core.plugrun import runAll
from core.utils import validateHost
from core.colors import color, G, O, R
from libs.data import VERSION as __version__
from libs.data import LICENSE as __license__

print('''
  %sSIPTorch %s- %sA SIP Torture Testing Suite
           %sVersion : v%s%s
''' % (color.CYAN, color.GREY, color.BLUE, color.RED, __version__, color.END))

log = logging.getLogger('options')

parser = argparse.ArgumentParser(usage='./siptorch.py -u <url/ip> [options]')
parser._action_groups.pop()

required = parser.add_argument_group('Required Arguments')
optional = parser.add_argument_group('Optional Arguments')

# Required arguments
required.add_argument('-u', '--target', help='Destination target to test', dest='target', type=str)

# Optional arguments
optional.add_argument('-p', '--rport',
                help='Destination port to use for sending packets to (default 5060)', dest='rport', type=int)
optional.add_argument('-P', '--lport',
                help='Local source port to use for binding to (default 5060)', dest='lport', type=int)
optional.add_argument('-o', '--output',
                help='Output directory to write results to', dest='output', type=str)
optional.add_argument('-d', '--delay', 
                help='Specify delay in seconds between two subsequent requests', dest='delay', type=int)
optional.add_argument('-t', '--timeout', 
                help='Timeout value in seconds', dest='timeout', type=int)
optional.add_argument('-v', '--verbose', 
                help='Increase output verbosity, multiple -v increase verbosity', dest='verbose', action='count')
optional.add_argument('-q', '--quiet',
                help='Decrease verbosity to lowest level', dest='quiet', action='store_true')
optional.add_argument('-V', '--version',
                help='Display the version number and exit', dest='version', action='store_true')
#optional.add_argument('--check-update'
#                help='Checks if a new update is available', dest='update', action='store_true')
optional.add_argument('--user-agent', 
                help='Use custom user-agent', dest='user_agent', type=str)
optional.add_argument('--spoof-ua', 
                help='Spoof user-agents with every request', dest='spoof_ua', action='store_true')
optional.add_argument('--build-cache',
                help='Build the modules cache (when a new module has been added)', dest='build_cache', action='store_true')
args = parser.parse_args()

if not len(sys.argv) > 1:
    parser.print_help()
    sys.exit(1)

if args.version:
    print(G, 'SIPTorch Version: %s' % __version__)
    print(G, 'SIPTorch License: %s' % __license__)
    sys.exit(0)

if args.build_cache:
    print(O, 'Building cache...')
    runAll(args)
    print(G, "Cache successfully built.")
    sys.exit(G+" See the updated `modules.json` under libs/ folder.")

if args.user_agent:
    config.USER_AGENT = args.user_agent

if args.lport:
    config.LPORT = args.lport

if args.rport:
    config.RPORT = args.rport

if not (args.version and args.build_cache):
    if args.target:
        config.RHOST = args.target
        log.info('Testing target')
        ip = validateHost(config.RHOST)
        if not ip:
            log.fatal("Invalid target specified, please check your input")
            sys.exit(1)
        config.IP = ip
    else:
        log.fatal('You must specify a target via the -u/--url argument')
        sys.exit(1)

if args.delay:
    config.DELAY = args.delay

if args.timeout:
    config.TIMEOUT = args.timeout

if args.output:
    if os.path.isdir(args.output):
        config.OUTPUT_DIR = args.output
    else:
        log.fatal("Invalid output directory, please specify a correct path.")
        sys.exit(1)

if args.spoof_ua:
    log.info('Spoofing user-agent from now on')
    config.SPOOF_UA = True