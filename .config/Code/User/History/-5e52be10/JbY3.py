#!/usr/bin/env python3

# get random names from text files
import random as rn

female = ''
male = ''
last = ''
first = ''

def random_last():
    with open('txt/last_uni.txt') as last:
        last = rn.choice((last.read().splitlines()))
        return last

def random_first_male():
    with open('txt/first_male.txt') as male:
        male = rn.choice((last.read().splitlines()))
        return male

def random_first_female():
    with open('txt/first_female.txt') as female:
        female = rn.choice((last.read().splitlines()))
        return female
def random_first():
    with open('txt/first_male.txt') as male:
        male = last.read().splitlines()

    with open('txt/first_female.txt') as female:
        female = last.read().splitlines()

    first = male + female
    return rn.choice(first)