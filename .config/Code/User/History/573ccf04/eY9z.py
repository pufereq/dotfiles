#!/usr/bin/env python3
import platform
# os check

def check():
    os = platform.system().lower()
    if os == 'linux': os_id = 0
    elif os == 'windows': os_id = 1
    else: os_id = 2
    return os_id
print(check())