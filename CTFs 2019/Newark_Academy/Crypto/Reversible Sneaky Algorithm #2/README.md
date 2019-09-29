# Newark Academy CTF 2019 – Reversible Sneaky Algorithm #2

* **Category:** Crypto
* **Points:** 350

## Challenge

> Oligar was thinking about number theory at AwesomeMath when he decided to encrypt a message with RSA. As a mathematician, he made various observations about the numbers. He told Molly one such observation:

>a^r ≡ 1 (mod n)

> He isn't SHOR if he accidentally revealed anything by telling Molly this fact... can you decrypt his message?

> Source code, a and r, public key, and ciphertext are attached.

## Hint 

> I'm pretty SHOR Oligar was building a quantum computer for something...


## Solution

In this task we should use Shor's algorithm - a quantum computer algorithm for integer factorization.

In short:
1) find minimal r: a**r == 1 mod N
Fortunately, such a and r are given in the task.

2) calculate q = gcd(a**(r/2) +1, N)

Now we know factorization, so we can easily calculate phi(N) and decrypt message.

See solver.py