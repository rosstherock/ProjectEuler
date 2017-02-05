"""
The Poly class can be used to add and multiply polynomials.
"""

class Poly:

    def __init__(self,C):
        self.C = C

    def __str__(self):
        return str(self.C)

    def __add__(self,other):
        c = [0] * max(len(self.C),len(other.C))
        for i in range(len(self.C)):
            c[i] += self.C[i]
        for i in range(len(other.C)):
            c[i] += other.C[i]
        while len(c)>0 and c[-1]==0:
            c.pop()
        return Poly(c)

    def __mul__(self,other):
        c = [0]*(len(self.C)+len(other.C)-1)
        for i in range(len(self.C)):
            for j in range(len(other.C)):
                c[i+j] += self.C[i]*other.C[j]
        return Poly(c)

def getPolyFromRoots(roots):
    """
    returns the monic polynomial with a given list of roots.
    """
    ret = Poly([1])
    for r in roots:
        ret *= Poly([-r,1])
    return ret
