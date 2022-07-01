#!/usr/bin/env python3

# get random names from text files
import random as rn

female = ''
male = ''
last = ''

def get_names():
    with open('txt/last_uni.txt').read() as last:
        print(last)