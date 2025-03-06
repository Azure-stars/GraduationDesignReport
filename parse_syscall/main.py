# Description: Extract syscall list from strace log file
import argparse
argparser = argparse.ArgumentParser()
argparser.add_argument('-s', '--strace_log', type=str, help='strace log file')
args = argparser.parse_args()

STRACE_LOG = args.strace_log
SYSCALL_LIST = set()

with open(STRACE_LOG + '.log', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if '(' not in line:
            continue
        # If using strace -f to trace, the first field of each line is the pid, so we need to remove it
        if line[0].isdigit():
            line = line.split(' ', 1)[1]
        syscall = line.split('(')[0]
        # Remove blank space for syscall
        syscall = syscall.strip()
        # Remove useless information
        if syscall.find('<') != -1 or syscall.find('+') != -1 or syscall.find('?') != -1:
            continue
        if syscall not in SYSCALL_LIST:
            SYSCALL_LIST.add(syscall)

with open(STRACE_LOG + '_syscall_list.txt', 'w') as f:
    for syscall in SYSCALL_LIST:
        f.write(syscall + '\n')