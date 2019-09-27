# Newark Academy CTF 2019 – Dr. J's Group Test Randomizer: Board Problem #0

* **Category:** Crypto
* **Points:** 100

## Challenge

>Dr. J created a fast pseudorandom number generator (prng) to randomly assign pairs for the upcoming group test. Leaf really wants to know the pairs ahead of time... can you help him and predict the next output of Dr. J's prng? Leaf is pretty sure that Dr. J is using the middle-square method.

>The server is running the code in class-randomizer-0.c. Look at the function nextRand() to see how numbers are being generated!

##Hint:

>The middle-square method is completely determined by the previous random number... you can use a calculator and test that this is true!

## Solution

If we look at nextRand() func, we'll se that previous "random" number defines next one.

If we will translate func from c to python, we will get:

seed = int(str(seed)[-12:-4])**2

After we get the first number, we can guess second, third and so on using the equation above.