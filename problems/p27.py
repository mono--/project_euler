# this implements the sieve of eratosthenes

# we need to quickly remove the first element of our 'list' 
# hence use queues!
from collections import deque
all_numbers=deque()

limit=2*10**5   #all primes below this limit should be summed. this must be even!
primes=list()   #no primes discovered so far

def precompute_primes():

# 2 is the first prime
    primes.append(2)
    print(2)

# the next number (3) is also prime
    all_numbers.append(True)

# now initialize the primeness of all numbers up to 'limit' with our current
# knowledge: all even numbers are not prime

    k=0 # k will be the difference between last prime discovered and current number
    for i in range(1,(limit/2)-1):
        all_numbers.append(False)
        all_numbers.append(True)
    all_numbers.append(False)

    while True:
        # get the next number in queue and check if it is prime, according to
        # knowledge
        try: 
            t=all_numbers.popleft()
            if t==True:
                k=k+1
                last=primes.pop() #remind ourselves of the highest prime we know
                primes.append(last) # write it down again, since 'pop' pops it
                primes.append(last+k) #write the new prime
                print(last+k)
                # now update our knowledge: all multiples of the new prime are 
                # no primes
                i=1
                while i*(last+k) <= len(all_numbers):
                    all_numbers[i*(last+k)-1]=False
                    i=i+1
                # we discovered a new prime, so difference to it is 0
                k=0
            else:
                # we didn't discover a new prime, so next number has higher
                # difference to last prime
                k=k+1
        #if queue is empty, we are done
        except:
                return primes



def main():
    primes = set(precompute_primes())
    print len(primes)
    A=-999
    B=-999
    m=0
    for a in range (-999,1000):
        for b in range (-999,1000):
            n=0
            while n*n+a*n+b in primes:
                n=n+1
                if n > m: #we hit a new record!
                    m=n 
                    A=a
                    B=b
    print "A und B sind"
    print str(A) + ", " + str(B)
    print "m ist"
    print m
main()
