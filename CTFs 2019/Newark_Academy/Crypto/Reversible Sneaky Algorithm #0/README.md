# Newark Academy CTF 2019 – Reversible Sneaky Algorithm #0

* **Category:** Crypto
* **Points:** 125

## Challenge

> Yavan sent me these really large numbers... what can they mean? He sent me the cipher "c", the private key "d", and the public modulus "n". I also know he converted his message to a number with ascii. For example:

> "nactf" --> \x6e61637466 --> 474080310374

> Can you help me decrypt his cipher?

## Hint

## Solution

There are chipertext(c), private exponent(d) and modulus(n) in rsa0.txt

We should calculate c**d % n to get a plaintext and convert it to bytes.
