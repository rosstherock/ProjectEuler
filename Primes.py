# A library of custom functions relating to prime numbers.
#
# Author: Ross Atkins
# Date Created: September 2015
#
# These functions were used to solve various Project Euler Problems
# Project Euler Problems can be found at https://projecteuler.net/archives

def getPrimes(N):
    """
    Calculates and returns a sorted list of all prime numbers at most N.
    """
    N = int(N)
    isPrime = [False,False,True] + [True,False]*(N>>2)
    for p in range(3,int(N**0.5)+1,2):
        if not isPrime[p]: continue
        for q in range(p**2,N+1,2*p):
            isPrime[q]=False
    return [p for p in range(N+1) if isPrime[p]]

def gcd(A,B):
    """
    calculates and returns the greatest common divisor of A and B.
    returns 0 if both A and B equal 0.
    """
    a,b=abs(A),abs(B)
    while b>0:
        a,b=b,a%b
    return a

def modInverse(A,M):
    """
    calculates and returns the multiplicative inverse of A modulo M.
    returns 0 if A and M have a common factor greater than one.
    """
    b = abs(M)
    a = A%b
    quotients = []
    while a>0:
        quotients.append(b//a)
        a,b = b%a,a
    # b is now the gcd of A and M.
    if b!=1:
        return 0 # A and M were not coprime.
    x,y=1,0
    for q in reversed(quotients):
        x,y = y,x+q*y
    if len(quotients)%2==1:
        return y
    return M-y

def isPrime(N):
    """
    Returns True if N is probably prime.
    Returns False if we found a witness to the compositeness of N.
    Valid for all N up to 3317044064679887385961980.
    """
    d,r = N-1,0
    while not d%2:
        d,r = d>>1, r+1
    if N<1373653:
        return any(_rabin_miller(a,d,N,r) for a in (2,3))
    if N<341550071728321:
        return any(_rabin_miller(a,d,N,r) for a in (2,3,5,7,11,13,17))
    return any(_rabin_miller(a,d,N,r) for a in (2,3,5,7,11,13,17,19,23,29,31,37,41))

def _rabin_miller(A,D,N,R):
    # This is the Rabin-Miller algorithm used only as part of the isPrime(N) function.
    if pow(A,D,N) == 1:
        return True
    res = pow(A,D,N)
    if res==N-1:
        return True
    for s in range(1,R):
        res = pow(res,2,N)
        if res==N-1:
            return True
    return False # n  is composite

def totient(N,Primes):
    """
    computes and returns the euler-totient function of N.
    This method will work whenever all the prime divisors (up to N**0.5)
    of N are in the sorted list Primes.
    Such a list can be generated using getPrimes(M) for some M>N**0.5,
    but there is no need to do this each time totient(N) is called.
    """
    tot = N
    for p in Primes:
        if p**2>N: break
        if N//p!=0: continue
        N//=p
        tot //= p
        tot *= p-1
        while N%p==0:
            N//=p
    if N>1:
        tot //= N
        tot *= N-1
    return tot

def getPrimeDivisors(N,primes):
    """
    computes and returns a sorted list of all prime divisors of N.
    This method will work whenever all the prime divisors (up to N**0.5)
    of N are in the sorted list Primes.
    Such a list can be generated using getPrimes(M) for some M>N**0.5,
    but there is no need to do this each time totient(N) is called.
    """
    div = []
    for p in Primes:
        if p**2>N: break
        if N//p!=0: continue
        N//=p
        div.append(p)
        while N%p==0:
            N//=p
    if N>1:
        div.append(N)
    return div

def getPrimeFactorisation(N,primes):
    """
    computes and returns a sorted list of all prime divisors of N.
    This method differs from getPrimeDivisors(N,Primes) only
    because it counts the multiplicity of each prime divisor.
    This method will work whenever all the prime divisors (up to N**0.5)
    of N are in the sorted list Primes.
    Such a list can be generated using getPrimes(M) for some M>N**0.5,
    but there is no need to do this each time totient(N) is called.
    """
    pfact = []
    for p in Primes:
        if p**2>N: break
        if N//p!=0: continue
        N//=p
        pfact.append(p)
        while N%p==0:
            N//=p
            pfact.append(p)
    if N>1:
        pfact.append(N)
    return pfact
