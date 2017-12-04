def pe44():
    ps = set()
    i = 0
    while True:
        i += 1
        p = (3*i*i - i) / 2
        ps.add(p)
        for n in ps:
            if p-n in ps and p-2*n in ps: 
                return p-2*n

print "Project Euler 44 Solution =", pe44()

import math

def pent(n):
    return n*(3*n-1)/2
    
def is_penta(k):
    n=1/6+math.sqrt(1/36+2*k/3)
    if n*(3*n-1)/2==k:
        return True
    else:
        return False
        
d=0
while True:
    d=d+1
    #print d
    r=int(math.ceil((3*d^2-d+4)/6))
    for i in range (r+1):
        for j in range(r+1):
            if pent(i)==pent(j)+pent(d):
                if is_penta(pent(i)+pent(j)):
                    print i,j
                    break

    

