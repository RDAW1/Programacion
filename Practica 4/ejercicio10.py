print 'Escribe el alto del triangulo'
a=input()
b=1
c=a-1
for f in range(a):
    for i in range(1):
        for g in range(c):
            print ' ',
        for h in range(b):
            print '*',
        b=b+2
        c=c-1
        print
