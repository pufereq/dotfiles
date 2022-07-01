#!/usr/bin/env python3
import platform
# os check

def check():
    os = platform.system().lower
    print(os)
check()