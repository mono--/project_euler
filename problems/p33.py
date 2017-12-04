def commondigit(a,b):
    a_set=set(str(a))
    b_set=set(str(b))
    return a_set & b_set

i=0
l=[]
for n in range(10,100):
    for m in range(n+1,100):
        if len(commondigit(m,n)) > 0:
            i=i+1
#            print str(n)+" "+str(m)
            l.append([n,m])

for x in l:
    n_str=str(x[0])
    m_str=str(x[1])
    for d in commondigit(x[0],x[1]):
        if n_str != str(d)+str(d):
            n=int(n_str.replace(str(d),""))
        else:
            break
        if m_str != str(d)+str(d):
            m=int(m_str.replace(str(d),""))
        else:
            break
        if n*x[1]==x[0]*m and not x[0] % 10 == 0:
            print str(x[0])+" divided by "+str(x[1])+" is " + str(n)+" divided by " +str(m)

