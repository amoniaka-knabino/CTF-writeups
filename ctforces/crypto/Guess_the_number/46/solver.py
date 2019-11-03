"""
We need a pseudoprime, Carmichael number.
We can find it using Chernick criteria
https://math.stackexchange.com/questions/2295095/what-is-the-fastest-way-to-get-the-next-carmichael-number
"""

from gmpy2 import is_prime

def Chernick_criteria(k):
    a = is_prime(6*k+1)
    b = is_prime(12*k+1)
    c = is_prime(18*k+1)
    return a and b and c

for k in range(pow(2,250), pow(2,260)):
    if Chernick_criteria(k):
        print("FOUND! " + str((6*k+1)*(12*k+1)*(18*k+1)))
        break
