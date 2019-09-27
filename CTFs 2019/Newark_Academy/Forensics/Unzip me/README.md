# Newark Academy CTF 2019 – Unzip Me

* **Category:** forensics
* **Points:** 150

## Challenge
fcrackzip -D -p rockyou.txt -u zip1.zip
> I stole these files off of The20thDucks' computer, but it seems he was smart enough to put a password on them. Can you unzip them for me?

## Hint

>There are many tools that can crack zip files for you

>All the passwords are real words and all lowercase

## Solution

If password is a real word, we can crack crack it by dictionary.
This challenge is easily solved using fcrack (https://github.com/hyc/fcrackzip) and "rockyou" doctonary.

fcrackzip -D -p rockyou.txt -u zipX.zip

You will get textfiled with 3 parts of the flag after unzipping.