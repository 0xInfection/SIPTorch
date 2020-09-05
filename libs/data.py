#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

VERSION = '0.1.0'
LICENSE = 'GNU General Public License v3 (GPLv3)'

# Whitespace chars
TAB = r"	"
WS = r" "
EN_QUAD = r" "
EM_QUAD = r" "
IDG_SEP = r"　"

# Null char
NULL_CHAR = r"%00"

# Backslash sequence to insert
BACKSLASH_SEQ1 = r'\\\"'
BACKSLASH_SEQ2 = r'\"\"'

# Response mapping
RESP_MAP = {  
    "100" : "Trying",
    "180" : "Ringing",
    "181" : "Call is Being Forwarded",
    "182" : "Queued",
    "183" : "Session in Progress",
    "199" : "Early Dialog Terminated",
    "200" : "OK",
    "202" : "Accepted",
    "204" : "No Notification",
    "300" : "Multiple Choices",
    "301" : "Moved Permanently",
    "302" : "Moved Temporarily",
    "305" : "Use Proxy",
    "380" : "Alternative Service",
    "400" : "Bad Request",
    "401" : "Unauthorized",
    "402" : "Payment Required",
    "403" : "Forbidden",   
    "404" : "Not Found",
    "405" : "Method Not Allowed",
    "406" : "Not Acceptable",
    "407" : "Proxy Authentication Required",
    "408" : "Request Timeout",
    "409" : "Conflict",
    "410" : "Gone",
    "411" : "Length Required",
    "412" : "Conditional Request Failed",
    "413" : "Request Entity Too Large",
    "414" : "Request-URI Too Long",
    "415" : "Unsupported Media Type",
    "416" : "Unsupported URI Scheme",
    "417" : "Unknown Resource-Priority",
    "420" : "Bad Extension",
    "421" : "Extension Required",
    "422" : "Session Interval Too Small",
    "423" : "Interval Too Brief",
    "424" : "Bad Location Information",
    "428" : "Use Identity Header",
    "429" : "Provide Referrer Identity",
    "430" : "Flow Failed",
    "433" : "Anonymity Disallowed",
    "436" : "Bad Identity-Info",
    "437" : "Unsupported Certificate",
    "438" : "Invalid Identity Header",
    "439" : "First Hop Lacks Outbound Support",
    "470" : "Consent Needed",
    "480" : "Temporarily Unavailable",
    "481" : "Call/Transaction Does Not Exist",
    "482" : "Loop Detected",
    "483" : "Too Many Hops",
    "484" : "Address Incomplete",
    "485" : "Ambiguous",
    "486" : "Busy Here",
    "487" : "Request Terminated",
    "488" : "Not Acceptable Here",
    "489" : "Bad Event",
    "491" : "Request Pending",
    "493" : "Undecipherable",
    "494" : "Security Agreement Required",
    "500" : "Server Internal Error",
    "501" : "Not Implemented",
    "502" : "Bad Gateway",
    "503" : "Service Unavailable",
    "504" : "Server Time-out",
    "505" : "Version Not Supported",
    "513" : "Message Too Large",
    "580" : "Precondition Failure",
    "600" : "Busy Everywhere",
    "603" : "Decline",
    "604" : "Does Not Exist Anywhere",
    "606" : "Not Acceptable"
}

BAD_RESP = ['100', '182', '486', '600']

URL_MAP = {
    "0"  :  "%30",
    "1"  :  "%31",
    "2"  :  "%32",
    "3"  :  "%33",
    "4"  :  "%34",
    "5"  :  "%35",
    "6"  :  "%36",
    "7"  :  "%37",
    "8"  :  "%38",
    "9"  :  "%39",
    "A"  :  "%41",
    "B"  :  "%42",
    "C"  :  "%43",
    "D"  :  "%44",
    "E"  :  "%45",
    "F"  :  "%46",
    "G"  :  "%47",
    "H"  :  "%48",
    "I"  :  "%49",
    "J"  :  "%4A",
    "K"  :  "%4B",
    "L"  :  "%4C",
    "M"  :  "%4D",
    "N"  :  r"%4E",
    "O"  :  r"%4F",
    "P"  :  "%50",
    "Q"  :  "%51",
    "R"  :  "%52",
    "S"  :  "%53",
    "T"  :  "%54",
    "U"  :  "%55",
    "V"  :  "%56",
    "W"  :  "%57",
    "X"  :  "%58",
    "Y"  :  "%59",
    "Z"  :  "%5A",
    "_"  :  r"%5F",
    "a"  :  "%61",
    "b"  :  "%62",
    "c"  :  "%63",
    "d"  :  "%64",
    "e"  :  "%65",
    "f"  :  "%66",
    "g"  :  "%67",
    "h"  :  "%68",
    "i"  :  "%69",
    "j"  :  "%6A",
    "k"  :  "%6B",
    "l"  :  "%6C",
    "m"  :  "%6D",
    "n"  :  r"%6E",
    "o"  :  r"%6F",
    "p"  :  "%70",
    "q"  :  "%71",
    "r"  :  "%72",
    "s"  :  "%73",
    "t"  :  "%74",
    "u"  :  "%75",
    "v"  :  "%76",
    "w"  :  "%77",
    "x"  :  "%78",
    "y"  :  "%79",
    "z"  :  "%7A",
}

LONGSHORT_MAP = {
    'accept-contact'    :   'a',
    'referred-by'       :   'b',
    'content-type'      :   'c',
    'content-encoding'  :   'e',
    'from'              :   'f',
    'call-id'           :   'i',
    'supported'         :   'k',
    'content-length'    :   'l',
    'contact'           :   'm',
    'event'             :   'o',
    'refer-to'          :   'r',
    'subject'           :   's',
    'to'                :   't',
    'allow-events'      :   'u',
    'via'               :   'v'
}

SCHAR_MAP = {
    "[" :  "%5B",
    "]" :  "%5D",
    "^" : r"%5E",
    "_" : r"%5F",
    "`" :  "%60",
    ":" :  "%3A",
    ";" :  "%3B",
    "<" :  "%3C",
    "=" :  "%3D",
    ">" : r"%3E",
    "?" : r"%3F",
    "@" :  "%40",
    "!" :  "%21",
    '"' :  "%22",
    "#" :  "%23",
    "$" :  "%24",
    "%" :  "%25",
    "&" :  "%26",
    "'" :  "%27",
    "(" :  "%28",
    ")" :  "%29",
    "*" :  "%2A",
    "+" :  "%2B",
    "," :  "%2C",
    "-" :  "%2D",
    "{" :  "%7B",
    "|" :  "%7C",
    "}" :  "%7D",
    " " :  "%20",
}