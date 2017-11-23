from functools import wraps
import re
import subprocess
import time


class FaultCode(Exception):
    pass

class FaultCode23(FaultCode):
    pass

class FaultCode36(FaultCode):
    pass

class FaultCode37(FaultCode):
    pass

class FaultCode55(FaultCode):
    pass


exc_map = {
    23: FaultCode23,
    36: FaultCode36,
    37: FaultCode37,
    55: FaultCode55,
}


logpath = 'logfile.txt'
def logtime(func):
    @wraps(func)
    def f(*args, **kwargs):
        log_format = '{} - {} - {}\n'
        logtime = time.time()
        try:
            return_val = func(*args, **kwargs)
        except FaultCode as e:
            log_status = 'FAULT CODE: ' + str(e) + '\n'
            with open(logpath, 'a') as f:
                f.write(log_format.format(logtime, args[0], log_status))
            raise
        log_status = 'SUCCESS'
        with open(logpath, 'a') as f:
            f.write(log_format.format(time.time(), args[0], log_status))
        return return_val
    return f


@logtime
def send_command_sub(command):
    printout = subprocess.check_output(['python', 'bsc.py', '"{}"'.format(command)])
    fc_regex = r"FAULT CODE (\d+)"
    fc_search = re.search(fc_regex, printout)
    if fc_search:
        fc = fc_search.group(1)
        raise exc_map.get(fc, FaultCode)(fc)
    return printout


def send_with_rerties(command, max_retries):
    try:
        return send_command_sub(command)
    except FaultCode:
        if max_retries > 0:
            return send_with_rerties(command, max_retries-1)
        else:
            print "max retries exceeded", command


cmdlist = [
        ('NTSTP;', 3),
        ('EXRPP;', 2),
        ('PLLDP;', 4),
        ('EXEMP;', 1),
        ]


def upgrade():
    for cmd, retries in cmdlist:
        send_with_rerties(cmd, retries)


if __name__ == '__main__':
    open(logpath, 'w').close()
    upgrade()
