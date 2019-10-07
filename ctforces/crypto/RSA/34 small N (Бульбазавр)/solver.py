'''
https://ctforces.com/tasks/34/

The main idea - small N (64 bit) can be bruteforce easily.
'''

from Crypto.PublicKey import RSA
from math import sqrt
from sys import argv
from gmpy2 import invert, mpz
from Crypto.Util import number

def factorize(n):
    '''
    https://www.quaxio.com/exploring_three_weaknesses_in_rsa/
    '''
    if n%2==0:
        return 2
    if n%3==0:
        return 3
    if n%5==0:
        return 5
    m = sqrt(n)
    i=7
    while i<=m:
        if (n%i==0):
            return i
        if (n%(i+4)==0):
            return i+4
        if (n%(i+6)==0):
            return i+6
        if (n%(i+10)==0):
            return i+10
        if (n%(i+12)==0):
            return i+12
        if (n%(i+16)==0):
            return i+16
        if (n%(i+22)==0):
            return i+22
        if (n%(i+24)==0):
            return i+24
        i+=30


with open('key.pem', 'r') as key_file:
    key = key_file.read()
pubkey = RSA.importKey(key)

n = pubkey.n #n = 7616284578445597693; len(bin(n)) == 64
e = pubkey.e  # e = 65537

#n is very small, so we can easily brute-force it!
#it takes only several minutes
p = factorize(pubkey.n) #p = 2472945799
q = n//p # q = 30798429077

#if we now factorization, we can easily calculate private exponent
# e * d == 1 (mod phi) => d = invert(e, phi) 
phi = (p-1)*(q-1)
d = invert(mpz(e),mpz(phi)) 

#now we should just read flag and decrypt it with private key
with open('flag.enc', 'rb') as flag_file:
    flag = flag_file.read()
flag_int = number.bytes_to_long(flag)
decr_flag_int = pow(flag_int, int(d), n)
decr_flag = number.long_to_bytes(decr_flag_int)
print(str(decr_flag))


