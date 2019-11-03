#!/usr/bin/env sage
"""
Partial key exposure attack
source: ???
"""

from sage.all import *

E = 53
P = 2
L = 716
mod = P**L

if 1:
    # challenge
    E,C,N = (
        53,
       59373582008105456633285804492879793275976175215548506440640425488332636264373119548200131380955989193205613148221059145000340530960128386811743358381812729316187573315576217705953540384008369081237614397216898070300396175001085836343942954068738894416230337425045092823173788543182037152264702032805902237160
,
        82209313643772832551477004354045765764684545506597655098636693898559086173055616023485297086353788799015613182305480165400975436534257677545987515254033212507792461917044228536506231139881256362102222015034268521262354212272584123870169983453094661472567948328096513225460826532945646507293865284255313621101,
    )
    dlow = int("10100111010010111110001111001000000101100001011010010100111010101011111011100011101111111110010010101011101011110110111111111000100100001001010100011111011101100010011111100000000001010111100010000101111001100110000001110000110001000000110010100101101011110100100100110101101101010010100110101000101010101100101111100011010111100111100010111100001101010110110000111010110010111111111001010111100111111011010010010001000110010110110011000001101100010011000001111011111110100110111010011010100100110101010110110000011110000000111110111010100011101100001010101000110101100010110011110110101101110011110010101111100110001000000010011110110000111010000111001001010011101111000100100101111110100010001001011101010011011101", 2)

    p = q = None
    start_k = 1
else:
    # local test: generate random case
    p = next_prime(randint(1, 2**512-1))
    q = next_prime(randint(1, 2**512-1))
    N = p * q
    print "p", p
    print "q", q
    print float(log(p, N))
    print float(log(q, N))
    phi = (p-1)*(q-1)
    D = inverse_mod(E, phi)
    C = pow(0x31337, E, N)
    dlow = D % (P**L)
    print "K=", E * D // phi
    start_k = E * D // phi

def solve_quadratic_mod_power(a, b, c, p, e):
    roots = {0}
    for cure in xrange(1, e + 1):
        roots2 = set()
        curmod = p**cure
        for xbit in xrange(p):
            for r in roots:
                v = r + (xbit * p**(cure - 1))
                if (a*v*v + b*v + c) % curmod == 0:
                    roots2.add(v)
        roots = roots2
    return roots

def calc_epsilon(N, X, beta):
    return float(beta**2 - log(2*X)/log(N))

x = PolynomialRing(Zmod(N), names='x').gen()
imod = inverse_mod(mod, N)

for k in xrange(start_k, E):
    a = k
    b = E*dlow - k*N - k - 1
    c = k*N
    for plow in solve_quadratic_mod_power(a, b, c, p=P, e=L):
        print "k", k, "plow", plow
        assert (a * plow**2 + b*plow + c) % mod == 0

        # poly = (x * mod + plow)  but .small_roots want it to be monic,
        # so multiply by inverse of mod (modulo N)
        poly = (x + plow * imod)
        # 0.49 to catch both primes, or 0.5 to catch the highest only
        beta = 0.5
        # math.log(2**512/10**97, 2): 189.77297479592588
        # so 2**200 is enough
        epsilon = calc_epsilon(N=N, X=2**193, beta=beta)

        roots = poly.small_roots(beta=beta, epsilon=epsilon)

        if not roots:
            continue

        print "Roots", roots
        root = int(roots[0])

        kq = root + plow * imod
        q = gcd(N, kq)
        assert 1 < q < N, "Fail"
        p = N // q
        D = inverse_mod(E, (p - 1) * (q - 1))
        msg = pow(C, D, N)
        print msg

        # convert to str
        h = hex(int(msg))[2:].rstrip("L")
        h = "0" * (len(h) % 2) + h
        print `h.decode("hex")`
quit()





