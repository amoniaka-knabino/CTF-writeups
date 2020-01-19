# TetCTF - padwith2019

* **Category:** Crypto
* **Solution authors:** amoniaka-knabino, MiKHalyCH

## Challenge

> Pad with 2019 in 2020! Let your past go!


## Solution

We had a server, which encrypt json file with AES-CBC with unusual padding, send it to us with IV and let us change it by sending encrypted bytes back.
Besides, server returns us different types of mistakes: decoding error and padding error.

json format: `{'admin': False, 'flag': open("flag1.txt").read()}`

We need to get 2 flags ( actually two parts of one ):

1st one - from json field 'flag'

2nd one will be given when we change `admin` from `False` to `True`

#### 1st flag

First of all, let's analyze json and split it into blocks. We will get something like:

```py
['\x02 {"admin": fals', 'e, "flag": "TetC','TF{***********"}']
```
Now it is clear that we need only last block.

Attack is very similar to [classical Padding-Oracle Attack on AES-CBC](https://robertheaton.com/2013/07/29/padding-oracle-attack/), but has some features, because:

1) padding function is unusual:

```py
PAD = bytes.fromhex("2019") * 8

def pad(s):
    pad_length = 16 - len(s) % 16
    return bytes([pad_length]) + PAD[:pad_length - 1] + s
```

2) plain text is padded at the beginning

To get to know 1st part of flag, we will send changed 3rd (penultimate, it will be IV for server) and 4st (last, it will be ciper-text) block of ciper-text.

We start from 1st byte of 3rd block.

1) Change the byte to \x00
2) Send the blocks to server
3) If we get answer 'incorrect padding', we change the byte to the next value and go to step 2. 
4) If we got another answer, it means that we can calculate the byte from original text (flag byte)
5) Store this byte and go to change 2nd byte

( See [1st solver](padwith2019_exploit_1flag.py) for details )

This way we can get all block and recover the first flag byte by byte.

#### 2nd flag

We want make `obj['admin']` == `True`. Here server doesn't check flag accuracy, so we can just change `obj` to `{"admin": true}`. This json will take one block with minimal padding (`\x01`).

We will send two blocks: `IV^(original_2nd_block_pt)^(desired_2nd_block_pt)` and `encrypted 2nd block`

We don't know padding value in original plaintext, so we will try several variant until attack is successful. (`'\x02 '` will be correct)

( See [2st solver](padwith2019_exploit_2flag.py) for details )



