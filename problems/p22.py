with open('p022_names.txt', "r") as f:
    names_str = f.read()
    names_stripped=names_str.strip('"')
    names=names_stripped.split('","')
    
#quicksort
def qsort1(l): 
    if l == []: 
        return []
    else:
        pivot = l[0]
        lesser = qsort1([x for x in l[1:] if x < pivot])
        greater = qsort1([x for x in l[1:] if x >= pivot])
        return lesser + [pivot] + greater

#namescores for all CAPITAL names!
def score(s):
    x=0
    for t in s:
        x=x+ord(t)-64
    return x

names=qsort1(names)

c=0 
for i in range(1,len(names)+1):
    c=c+score(names[i-1])*i

print c
