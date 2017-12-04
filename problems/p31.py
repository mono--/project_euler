c=[1,2,5,10,20,50,100,200]

def change(n,k):
    if n==0:
        return 1
    l=0
    for x in c:
        if n-x>=0 and x <=k:
            l=l+change(n-x,x)
    return l

print change(200,200)

