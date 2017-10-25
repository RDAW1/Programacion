print 'Escribe el alto del triangulo'
a=input()
b=1
d=1
c=a-1
s='*'


for i in range(a):
    for r in range(d):
        print s,
    d=d+1
    print

for i in range(c):
    for r in range(b,a):
        print s,
    b=b+1
    print 
        
        
    
