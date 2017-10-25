print 'Escribe un numero'
a=input()
print 'Escribe otro numero mayor que' ,(a)
b=input()
c=b+1
r=0
for i in range(a,c):
    r=i+r
print 'La suma desde' ,(a), 'hasta' ,(b), 'es' ,(r)
