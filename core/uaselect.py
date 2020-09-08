#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch


# This is a list of real SIP user-agents which have been
# handpicked from the wild. ;)
ualist = [
    'TANDBERG/4136 (X8.11.4)',
    'Home&Life HUB/1.1.26.00',
    'Sphairon UA - 2.27-2.9.15.2 NetConnect',
    'FRITZ!OS',
    'AVM FRITZ!Box Fon WLAN 7170',
    'TP-Link SIP Stack V1.0.0',
    'MediaAccess TG788vn v2 Build 10.5.2.S.GD',
    'FPBX-2.11.0(1.8.26.1)',
    'Yealink IPCALL 1.0.1.74',
    'STARFACE PBX',
    'Technicolor / VANT-6',
    'Thomson TG784 Build 8.4.2.Q',
    '3CXPhoneSystem 15.5.13103.5 (12071)',
    'Tilgin Vood HG238x_ESx415-02_10_01_24',
    'Mitel Border GW/4.11.0.163-01',
    'VOX30/XS_3.7.02.81',
    'FreeSWITCH-mod_sofia/1.4.26+git-20190329T162019Z~94024b0e35~64bit',
    'Sagem / HW_V0.0.1 / FW_V58C040-58C040 / SW_V1.2.344',
    'FPBX-14.0.13.23(13.22.0)',
    'FPBX-13.0.197.22(13.17.0)',
    'DLink VoIP Stack',
    'IPBX-2.11.0(11.25.3)',
    'Tilgin Vood HG23xx_DSx000-02_03_09_29',
    'Technicolor / AGTOT_2.1.3',
    'ARRIS-TM602G release v.6.1.120T.SIP SN/001DCDAA049F',
    'A510 IP/42.075.00.000.000',
    'Telasip SBC 5.2.3',
    'Wildix GW 20200619.1~587a822b',
    'dlink 12-3895-8588-1.3.3.244-ON201LW',
    'ZaiLab Conversation Switch',
    'CoreDialPBX',
    'FPBX-15.0.16.73(16.6.2)',
    'Technicolor / VANT-6 / AGTOT_1.0.4 / AGTOT_1.0.4',
]

import random
from mutators.replparam import genRandStr

def randUASelect(randstr=False, length=30):
    if randstr:
        return genRandStr(length, allow_digits=True)
    else:
        return random.choice(ualist)