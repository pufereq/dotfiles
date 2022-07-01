#!/usr/bin/env python3

import platform
# os check

os_id = 0

def __init__():
    # global os_id
    os = platform.system().lower()
    if os == 'linux': os_id = 0
    elif os == 'windows': os_id = 1
    else: os_id = 2
    return os_id

def clear():
    # global os_id
    if os_id == 0: return 'clear'
    elif os_id == 1: return 'cls'
    elif os_id == 2: return 'clear'
