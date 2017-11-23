# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import sys

from functools import partial
from random import randint

# wywolanie: python bsc.py "PCORP:BLOCK=MISSRA;" - muszą byc te cudzysłowy (przynajmniej dla basha)
helpstring = u"""Wywoływanie:
python bsc.py "KOMENDA:MML;" - uwaga na cudzysłowy
"""

command_re = r'(\w{5})[:]?(.*);'
try:
    command = sys.argv[1]
except IndexError:
    print(helpstring)
    sys.exit(1)

try:
    command, args = re.search(command_re, command).groups()
except AttributeError:
    print("""SYNTAX ERROR
FAULT CODE 0
BLA BLA BLA BLA
""")
    sys.exit(0)


def handle_command(good_printout, bad_printout):
    return [bad_printout, good_printout][randint(0, 1)]


# EXEMP
good = """<EXEMP:RP=ALL,EM=ALL;
EM DATA

RP    TYPE   EM  EQM                       TWIN  CNTRL  PP     STATE
   1  EPB1    0  RHLAPD-0                        PRIM          WO
   1  EPB1    1  AUCM-0                          PRIM          WO
   1  EPB1    2  RMPAG-0                         PRIM          WO
"""

bad = """<PLLDP;
NOT ACCEPTED
FAULT CODE 23
BLA BLA BLA BLA
"""
handle_exemp = partial(handle_command, good, bad)


# PLLDP
good = """<PLLDP;
PROCESSOR LOAD DATA
INT PLOAD CALIM  OFFDO OFFDI FTCHDO FTCHDI OFFMPH OFFMPL FTCHMPH FTCHMPL
 1    3    72000    38    16    38     16     26    171     26     171
 2    2    72000    34    11    34     11     31     29     31      29
 3    3    72000    57    19    57     19     35     47     35      47

INT OFFTCAP FTDTCAP
 1      0       0
 2      0       0
 3      0       0
END
"""

bad = """<PLLDP;
NOT ACCEPTED
FAULT CODE 55
BLA BLA BLA BLA
"""
handle_plldp = partial(handle_command, good, bad)


# NTSTP
good = """<NTSTP:SNT=ALL;
SWITCHING NETWORK TERMINAL STATE

SNT                SUBSNT  STATE     BLS LST              FCODE
ETM4-0                     WO
                   0       WO

END
"""

bad = """<NTSTP:SNT=ALL;;
NOT ACCEPTED
FAULT CODE 36
BLA BLA BLA BLA
"""
handle_ntstp = partial(handle_command, good, bad)


# EXRPP
good = """<EXRPP:RP=ALL;
RP DATA

RP    STATE  TYPE     TWIN  STATE   DS     MAINT.STATE  PIU
   1  WO     EPB1                          IDLE          1-22
   2  WO     EPB1                          IDLE          1-23
  81  WO     EVOET                         IDLE          1-3
END

"""

bad = """<EXRPP:RP=ALL;
NOT ACCEPTED
FAULT CODE 37
BLA BLA BLA BLA
"""
handle_exrpp = partial(handle_command, good, bad)


def handle_default():
    return """COMMAND NOT FOUND
FAULT CODE 1
COMMAND NOT FOUND
    """


commands_map = {
        'PLLDP': handle_plldp,
        'NTSTP': handle_ntstp,
        'EXEMP': handle_exemp,
        'EXRPP': handle_exrpp,
        }

print(commands_map.get(command.upper(), handle_default)())


