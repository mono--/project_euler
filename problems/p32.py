#generate list of all permutations of 1...9
l=[[]]

for i in range(1,10):
    m=[]
    for x in l:
        for k in range(1,10):
            if k not in x:
                m.append(x+[k])
    l=m

#print len(l) #this should yield 362880 :)


#convert list of digits to int
def convert(s):
    t=""
    for x in s:
        t=t+str(x)
    return int(t)


pan_numbers=[]
# check if a list of digits is pandigital
# note that the result of a*b=c must be at least 4 digits long
def pandig(s):
    for i in range(1,5): #i <= 7!
        for j in range(i+1,7): #i<=j
            if convert(s[:i])*convert(s[i:j])==convert(s[j:]):
                if convert(s[j:]) not in pan_numbers:
                    pan_numbers.append(convert(s[j:]))

for x in l:
    pandig(x)
    
print pan_numbers
print sum(pan_numbers)
