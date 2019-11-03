#!/usr/bin/env python3

import json
import gmpy2
import random
from Crypto.Util.number import isPrime

#config = json.load(open('config.json'))

#flag = config['FLAG']

flag = "CTF{you_are_win}"

def isCutePrime(n):
    for i in range(100):
        x = random.randint(1, pow(2, 1337))
        print("{} % n = {}".format(x, gmpy2.powmod(x,n-1,n)))
        if gmpy2.powmod(x, n - 1, n) != 1:
            return False
    return True

print("Gimme a good number")
try:
    p = int(input())
except:
    print("Incorrect input")
    exit(0)

if p < pow(2, 512):
    print("Too small")
    exit(0)

if not isCutePrime(p):
    print("It is not cute!!!")
    exit(0)

if isPrime(p):
    print("It is prime, DUDEEE!!1")
    exit(0)

print("Here is your flag: {}".format(flag))

