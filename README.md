<h1 align="center">
  <br>
  <a href="https://github.com/0xinfection/siptorch"><img src="https://i.imgur.com/Iux2GzGl.png" alt="siptorch"/></a>
  <br>
  <br>
  SIPTorch
</h1>
<h4 align="center">A "SIP Torture" (<a href="https://tools.ietf.org/html/rfc4475">RFC 4475</a>) testing suite.</h4>
<p align="center">  
  <a href="https://docs.python.org/3/download.html">
    <img src="https://img.shields.io/badge/Python-3.x-green.svg">
  </a>
  <a href="https://github.com/0xinfection/siptorch/releases">
    <img src="https://img.shields.io/badge/Version-v0.1%20(stable)-blue.svg">
  </a>
  <a href="https://github.com/0xinfection/siptorch/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-GNU%20GPLv3-orange.svg">
  </a> 
  <a href="https://travis-ci.org/0xInfection/siptorch">
    <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg?logo=travis">
  </a>
</p>

### About
__SIPTorch__ is a testing suite for the [Session Initiation Protocol](https://tools.ietf.org/html/rfc3261), popularly known as SIP Torture tests. These tests are primarily meant to harden and refine both the SIP protocol and its implementations. Hopefully this tool will help shaping SIP into a globally interoperable protocol for real time Internet communication services. 

Presently the tool implements the tests mentioned specifically in the [RFC 4475](https://tools.ietf.org/html/rfc4475), but future extensions to the modules is planned. The tests are divided into several sections - some stress the parser, some test the implementation of application/transaction layer semantics, some messages are themselves invalid, while others test backward compatibility. This tool however does not support IPv6 elements for now.

### Highlights
- [x] Implements full support for testing IPv4 elements.
- [x] [48 modules](#modules) crafted precisely for accurate tests.
- [x] User is in complete control of how the tool works.
- [x] Report generation functionality in markdown format.
- [x] Easily extensible modules library.

### Modules
Please have a look at the [`modules.json`](https://github.com/0xInfection/SIPTorch/blob/master/libs/modules.json) for detailed version:
- __Application Layer Semantics__
    - 200 OK Response with Broadcast Via Header Field Value
    - REGISTER with a Contact Header Parameter
    - REGISTER with a URL in Contact Header Parameter
    - INVITE Message Missing Required Header Fields
    - Unknown/Invalid Content Type
    - Invalid/Unacceptable Accept Offering
    - Zero Value in Max-Forwards Header
    - OPTIONS with Multiple Content-Length Values
    - Multiple Values in Single Value Required Fields
    - Request-URI with Known but Atypical Scheme
    - REGISTER with a URL Escaped Header
    - OPTIONS With Unknown Proxy-Require and Require Scheme
    - Unknown/Invalid Authorization Scheme
    - OPTIONS Request URI with Unknown Scheme
    - Unknown Request URI with Unknown Scheme in Header Fields
- __Backward Compatability Tests__
    - INVITE With RFC 2543 Syntax Support
- __Invalid Messages__
    - Invalid Time Zone in Date Header Field
    - Unterminated Quoted String in Display Names
    - Response with Overlarge Status Code
    - Content Length Larger Than Message
    - Request Method with CSeq Method Mismatch
    - Escaped Headers in SIP Request-URI
    - Extraneous Header Field Separators
    - Negative Content-Length
    - Non-token Characters in Display Name
    - `</>` Enclosing Request-URI
    - Multiple Space Separating Request-Line Elements
    - Malformed SIP Request-URI with Embedded LWS
    - Unknown Method with CSeq Method Mismatch
    - Negative Content-Length
    - Failure to Enclose name-addr URI in `<>`
    - Request Scalar Fields with Overlarge Values
    - Response Scalar Fields with Overlarge Values
    - Spaces Within Address Specification
    - Escaped Headers in SIP Request-URI
    - Unknown Protocol Version
- __Syntactical Parser Tests__
    - Extra Trailing Octets in a UDP Datagram
    - Use of `%` When It Is Not an Escape
    - Escaped Nulls in URIs
    - Valid Use of the `%` Escaping Mechanism
    - Long Values in Header Fields
    - Message with No LWS between Display Name and `<`
    - Multipart MIME Message
    - Content Length Larger Than Message
    - Semicolon-Separated Parameters in URI User Part
    - Varied and Unknown Transport Types
    - Unusual Reason Phrase
- Transaction Layer Semantics
    - Branch Tag Missing Transaction Identifier

### Installation
The only external requirement for this tool is the [`pluginbase`](https://pypi.org/project/pluginbase) library, which can be easily installed using `pip`:
```bash
python3 -m pip install pluginbase
```
or
```bash
python3 -m pip install -r requirements.txt
```

### Usage
Here is the help output from SIPTorch:
```
  SIPTorch - A SIP Torture Testing Suite
           Version : v0.1.0

usage: ./siptorch.py -u <url/ip> [options]

Required Arguments:
  -u TARGET, --target TARGET
                        Destination target to test

Optional Arguments:
  -p RPORT, --rport RPORT
                        Destination port to use for sending packets to (default 5060)
  -P LPORT, --lport LPORT
                        Local source port to use for binding to (default 5060)
  -o OUTPUT, --output OUTPUT
                        Output directory to write results to
  -d DELAY, --delay DELAY
                        Specify delay in seconds between two subsequent requests
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout value in seconds
  -v, --verbose         Increase output verbosity, multiple -v increase verbosity
  -q, --quiet           Decrease verbosity to lowest level
  -V, --version         Display the version number and exit
  --user-agent USER_AGENT
                        Use custom user-agent
  --spoof-ua            Spoof user-agents with every request
  --build-cache         Build the modules cache (when a new module has been added)
```
For a testbed, you'll require a URL/IP which talks SIP.  
For testing purposes you can use a publicly hosted testing server at `demo.sipvicious.pro`.

- Examples:
    - Basic example usage:
    ```bash
    ./siptorch.py -u sip.example.com --rport 5060 -v
    ```
    - Specify timeout and add delay between requests:
    ```bash
    ./siptorch.py -u sip.example.com --delay 2 --timeout 10
    ```
    - Spoof useragents with every request and add local port
    ```bash
    ./siptorch.py -u sip.example.com --spoof-ua --lport 5080 
    ```
    
After performing all the tests, the results of the tool are stored in a markdown file under the `siptorch-output/` folder in your current working directory.

For more advanced usage, you can have a look at the [configuration variables](https://github.com/0xInfection/SIPTorch/blob/master/libs/config.py) and edit them as per your need. Then fire up the tool as you would normally do.

### New modules
SIPTorch has been designed in a very flexible way so as to allow easy extension of modules. Writing a new module involves these steps:
- Decide which category of tests are you going to write a module on.
- Look at some examples of modules under the category, and write yours.
- Put it inside the specific folder under `modules/` directory.
- Run `./siptorch.py --build-cache` to generate the updated `modules.json`.
- Test the module on a target and check whether the results are intended.
- Submit a [pull request](https://github.com/0xInfection/SIPTorch/pulls). :)

### Version & License
The present codebase of SIPTorch is presently tagged as `v0.1.0` release. SIPTorch is licensed under the GNU General Public License (v3).
```bash
$ ./siptorch.py --version

  SIPTorch - A SIP Torture Testing Suite
           Version : v0.1.0

[+] SIPTorch Version: 0.1.0
[+] SIPTorch License: GNU General Public License v3 (GPLv3)
```

### Author's Words
This project was made by me out of sheer interest and curiousity when I was exploring the Session Initiation Protocol. The inspiration behind this is [sipvicious](https://github.com/enablesecurity/sipvicious) and my guru [Sandro Gauci](https://twitter.com/sandrogauci) who was gracious enough to allow me to explore this field under his wing. 

New ideas and pull requests are welcome. If you have any trouble, you can always [pull an issue up](https://github.com/0xInfection/SIPTorch/issues/new)!

> Crafted with ❤️ by [@0xInfection](https://twitter.com/0xInfection)