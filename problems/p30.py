l = [[a,b,c,d,e,f] for a in range(0,10) for b in range(0,10) for c in range(0,10)
 for d in range(0,10) for e in range(0,10) for f in range(0,10)]

summe=0
for x in l:
    t= sum([a**5 for a in x])
    s= ""
    for k in x:
        s=s+str(k)
    if t==int(s):
        print s
        summe=summe+t

print summe-1 #we don't want to count 1=1**5!
