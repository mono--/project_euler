from collections import deque

def add(a,b):
    l=max(len(a),len(b))
    a.extendleft([0]*(l-len(a)))
    #b.extendleft([0]*(l-len(b)))
    c=0 #carry
    r=deque(list()) #return vector
    for i in range(0,l):
        x=b[l-i-1]+a[l-i-1]+c
        r.appendleft(x % 10)
        c= x // 10
    r.appendleft(c)
    if r[0]==0:
        r.popleft()
    return r
    
a=deque([1])
b=deque([1])
i=2
while len(b) < 1000:
    c=add(a,b)
    a=b
    b=c
    i=i+1

print i
