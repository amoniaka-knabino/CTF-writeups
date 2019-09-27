# Newark Academy CTF 2019 – Filesystem Image

* **Category:** forensics
* **Points:** 200

## Challenge

> Put the path to flag.txt together to get the flag! for example, if it was located at ab/cd/ef/gh/ij/flag.txt, your flag would be nactf{abcdefghij}

## Hint

>Check out loop devices on Linux

## Solution

We got a filesystem image. I used fatcat for browsing it(https://github.com/Gregwar/fatcat)

Firstly, we need to * offset (tutorial: https://github.com/Gregwar/fatcat/blob/master/docs/partition.md)

It is 1*512 in our case.

When we'll try to extraxt using fatcat ./img.iso -O 512 -x DIRNAME

We will get such output:

>Extracting /lq/wk/zo/py/hu/flag.txt to DIRNAME/lq/wk/zo/py/hu/flag.txt
>They'll never find this! HAhahAHahAHAHaHAHAHAA
>:)
>Segmentation fault

The task is solved.


```
nactf{lqwkzopyhu}
```