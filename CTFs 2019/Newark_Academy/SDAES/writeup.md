# Newark Academy CTF 2019 – Super Duper AES

* **Category:** Crypto
* **Points:** 50

## Challenge

> The Advanced Encryption Standard (AES) has got to go. Spencer just invented the Super Duper Advanced Encryption Standard (SDAES), and it's 100% unbreakable. AES only performs up to 14 rounds of substitution and permutation, while SDAES performs 10,000. That's so secure, SDAES doesn't even use a key!

## Solution

As we can see (or guess) SDAES based on AES, symmetric algorithm.

We can easily invert algorithm from sdaes.py to decrypt chiper.txt

See solver.py