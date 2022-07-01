#!/usr/bin/env python3

# get random names from text files
import random as rn

female = ''
male = ''
last = ''

def random_last():
    with open('txt/last_uni.txt') as last:
        last = rn.choice((last.read().splitlines()))
        return last