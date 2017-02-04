"""
This is a complete solution to Project Euler problem 588 (https://projecteuler.net/problem=588).
The function Q(n) equals the number of odd quintinomial terms in the nth row.
We make use of the following mathematical identities:
Q(2*n) = Q(n)
Q(2**k*n+a) = Q(a) * Q(n) if a<2**(k-2)
"""

from Digits import getDigits


# given the nth row of quintinomial terms, this method returns the (n+1)th row.
def nextRow(row):
    temp = [0,0,0,0] + row[:] + [0,0,0,0]
    ret = []
    for n in range(len(row)+4):
        ret.append(sum(temp[n:n+5])%2)
    return ret

# given the nth row of quintinomial terms, this method returns the (n*2)th row.
def doubleRow(row):
    ret = [0]*(2*len(row)-1)
    for n in range(len(row)):
        ret[2*n] = row[n]
    return ret

# This method computes the nth row of quintinomial terms and then returns Q(n).
# This is slow because it takes O(n) space to store the list.
def Q_slow(n):
    digits = getDigits(n,2)
    row = [1]
    for d in reversed(digits):
        row = doubleRow(row)
        if d==1:
            row = nextRow(row)
    return sum(row)

# This is the main function.
def Q(n):
    # if n is even then Q(n) = Q(n//2).
    if n%2==0:
        if n==0:
            return 1
        return Q(n//2)
    # If p is a power of two and 4*a<p then Q(p*k+a) = Q(k) * Q(a).
    # We search to try to find such p.
    p=8
    while 4*(n%p)>p:
        p*=2
    if p<=n:
        return Q(n%p)*Q(n//p)
    # if no such p is small enough, then we compute Q(n) using a slow method.
    return Q_slow(n)

# The values of Q(10) and Q(100) are supposed to be 17 and 35.
print(Q(10))
print(Q(100))

# we are required to evaluate the sum of Q(10**k) for k=1,2,3,...,18.
ans = 0
for k in range(1,19):
    ans += Q(10**k)
print(ans)
