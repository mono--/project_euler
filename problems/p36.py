l= range(1,10**6+1)

def binary_string(n):
    return bin(n)[2:]

def palin(s):
    return all([s[i]==s[len(s)-i-1] for i in range(len(s))])
    
s=0
for n in l:
    n_str=str(n)
    n_binstr=binary_string(n)
    if palin(n_str) and palin(n_binstr):
        print n_str, n_binstr
        s=s+n
print "Sum is " + str(s)
