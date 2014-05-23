# Author  : Matan M. Mates
# File    : setup.py
# Purpose : Installer for Smart Debugger

import sys


def install():
   raise NotImplementedError()

def remove():
   raise NotImplementedError()

def print_usage():
    print("Usage: {} {install/remove}")

def main():
    if len(sys.argv) != 2:
        print_usage() 
        return -1

    script, command = sys.argv
    if command == 'install':
        return install()
    elif command == 'remove':
        return remove() 
    else:
        print_usage()
        return -2

if __name__ == '__main__':
    sys.exit(main())
