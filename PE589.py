"""
This is a complete solution to Project Euler problem 589 (https://projecteuler.net/problem=589).
numpy.linalg.solve() is used to solve a system of linear equations.
"""

import numpy.linalg as la

def R(m,n):
    A,B = [],[]
    for k in range(m+1):
        a,b = [0]*(m+1),0
        a[k] = (m-n+1)**2
        for i in range(n,m+1):
            for j in range(n,m+1):
                if j<k:
                    b += j
                else:
                    if i+k>=j:
                        b+=j
                        a[k+i-j]-=1
                    else:
                        b+=k+i
                        a[j-k-i]-=1
        A.append(a)
        B.append(b)
    X = la.solve(A,B)
    return X[0]

def E(m,n):
    return R(m+5,n+5)-5

print("E(60,30) = "+str(E(60,30)))

def S(k):
    start = time()
    ret = 0
    for m in range(2,k+1):
        for n in range(1,m):
            ret += E(m,n)
    return ret

print("S(5) = "+str(S(5)))

print("S(100) = "+str(S(100)))
