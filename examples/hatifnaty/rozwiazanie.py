from collections import OrderedDict
from datetime import  datetime
import os
import re
import subprocess


fc_regexp = r"FAULT CODE (\d+)"

logpath = 'logfile.txt'
def logger(func):
    def times(command):
        with open(logpath, 'ab') as f:
            f.write('execution of command {} started at date and time {}\n'.format(command, datetime.now()))
            printout = func(command)
            kotek = re.search(fc_regexp, printout)
            if kotek:
                f.write("RECEIVED FAULTCODE {}\n".format(kotek.group(1)))
            else:
                f.write("command finished successfully\n")
        return printout
    return times

@logger
def send_command(komenda):
    printout = subprocess.check_output(['python', 'bsc.py', '"{}"'.format(komenda)])
    return printout.decode('utf-8')


class MMLSyntaxError(Exception):
    pass


class CommandNotFound(Exception):
    pass


class ResponseError(Exception):
    pass


def fault_code_search(printout):
    syntax_fc = 0
    not_fpund_fc = 1
    response_fc = [23, 55, 36, 37]
    kotek = re.search(fc_regexp, printout)  # kotek oznacza czy jest FC czy nie XD
    if kotek:
        if int(kotek.group(1)) == syntax_fc:
            raise MMLSyntaxError(syntax_fc)
        if int(kotek.group(1)) == not_fpund_fc:
            raise CommandNotFound(not_fpund_fc)
        if int(kotek.group(1)) in response_fc:
            raise ResponseError(int(kotek.group(1)))


commands_dict = OrderedDict([
        ('PLLDP;', 2),  # liczba powtorzen to 2 czyli max wywolan to 3
        ('NTSTP;', 4),
        ('EXEMP;', 1),
        ('EXRPP;', 3),
        ])

def upgrade(commands):
    for i in commands:
        print 'command >> ', i
        repeated = 0
        while repeated < commands[i]:
            try:
                fault_code_search(send_command(i))
                break
            except (MMLSyntaxError, CommandNotFound, ResponseError):
                print 'exception >> ', repeated
                repeated += 1

open(logpath, 'w').close()
upgrade(commands_dict)
