l=1
g=1

for d in range(1,1000):
    i=1 #counter
    r=dict() #dictionary of when a remainder occured
    x=1 #current remainder
    while x not in r: #this remainder didn't occur
        r[x]=i
        x=x*10 % d
        i=i+1
    if i >= l: #neues maximum gefunden
        l=i-r[x]
        g=d

print l
print g
