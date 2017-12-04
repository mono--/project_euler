# easy recursion formula
# the problem is solved here

import time
def p(a,b):
    if a==0:
        return 1
    elif a==b:
        return 2*p(a-1,b)
    else:
        return p(a-1,b)+p(a,b-1)


# benchmarking, so you know what you can expect :-)
n=0
dt=0.0

while dt <= 0.1:
    n = n + 1
    t0 = time.time()
    x = p(n,n) #we don't use x
    dt = time.time()-t0

#compute two reference points of at least 0.1 second
t0=time.time()
x = p(n,n)
t1=time.time()-t0
n=n+1

t0=time.time()
x = p(n,n)
t2=time.time()-t0
n=n+1

t0=time.time()
x = p(n,n)
t3=time.time()-t0

e = (t3/t2 + t2/t1) / 2 # factor by which time increases for each step

k = int(raw_input("How far do you want me to go? (Enter natural number) \n"))

if k <= n-2:
    print "Expected running time is less than " + str(k/10) + " second(s)"
    print "Number of possibilities to cross grid: " + str(p(k,k))

if k >= n-1:
    print "Expected running time is " + str(e**(k-n)*t3) + " second(s)"
    r = raw_input("Do you want me to do this? (Y/N)")
    if r=="Y" or r=="y":
        t0=time.time()
        print "Number of possibilities to cross grid: " + str(p(k,k))
        print "Time taken: " + str(time.time()-t0)
    else:
        print "Stopping."
