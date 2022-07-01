#!/usr/bin/env python3

# get random names from text files
import random as rn

female = ''
male = ''
last = ''

def get_names():
    with open('txt/last_uni.txt') as last:
        rand_name = rn.choice((last.read().splitlines()))
        print(rand_name)