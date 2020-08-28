#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#     SIP Torch     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires SIPTorch
# https://github.com/0xInfection/SIPTorch

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