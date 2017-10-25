print 'Escribe un numero'
a=input()
print 'Escribe otro numero mayor que' ,(a)
b=input()
b=b+1
for i in range(a,b):
    if i % 2==0:
        print 'El numero' ,(i), 'es par'
    else:
        print 'El numero' ,(i), 'es impar'
