# Newark Academy CTF 2019 – Vyom's Soggy Croutons

* **Category:** Crypto
* **Points:** 50

## Challenge

> The close cousin of a website for "Question marked as duplicate" - part 2!

> Can you redirect code execution and get the flag?

## Hint

> pwntools can help you with crafting payloads

## Solution

If we look at bufover.c file, we will see a func "win" that we need to call.

The name of the task tells us that we should use buffer overflow attack.

Firstly, we should get to know win adress. We can do it using gdb (open bufoverfile and write "x win")

Secondly, we select right offset. Here it is 28.

After we craft payload with pwntools and send exploit.
