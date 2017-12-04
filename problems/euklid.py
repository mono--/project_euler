import math
def eea(a,b):
        if b == 0:
                return (a,1,0)
        (d,s,t)=eea(b,a % b)
        (c,u,v)=(d,t,s-math.floor(a/b)*t)
        return (c, u,v)
x=100001
y=2133
print(eea(x,y))
print(eea(x,y)[1])*x
print(eea(x,y)[2])*y
