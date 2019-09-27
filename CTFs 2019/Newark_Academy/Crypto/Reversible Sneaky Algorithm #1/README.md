# Newark Academy CTF 2019 – Reversible Sneaky Algorithm #1

* **Category:** Crypto
* **Points:** 275

## Challenge

> Lori decided to implement RSA without any security measures like random padding. Must be deterministic then, huh? Silly goose!

>She encrypted a message of the form nactf{****} where the redacted flag is a string of 4 lowercase alphabetical characters. Can you decrypt it?

>As in the previous problem, the message is converted to a number by converting ascii to hex.



## Solution

We know, that form of plaintext is "nactf{****}" where * = lowercase english letter.
Because there are only 26**4 variants, we can use brute-force attack.

```
nactf{pcks}
```
