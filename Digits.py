# A library of custom functions relating to decimal digits of integers.
#
# Author: Ross Atkins
# Date Created: September 2015
#
# These functions were used to solve various Project Euler Problems
# Project Euler Problems can be found at https://projecteuler.net/archives

def getDigits(N,base=10,length=0):
    """
    Computes and returns a list of the decimal digits of a positive integer.
    """
    ret = []
    if length==0:
        while N>0:
            ret.append(N%base)
            N//=base
    else:
        for i in range(length):
            ret.append(N%base)
            N//=base
    return ret

def getNumber(D,base=10):
    """
    Computes and returns an integer, given a list of it's decimal digits.
    """
    if len(D)==0:
        return 0
    i=len(D)-1
    ret = D[i]
    while i>0:
        i -= 1
        ret *= base
        ret += D[i]
    return ret
