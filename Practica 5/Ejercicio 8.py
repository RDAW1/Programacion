print 'Escribe un limite'
a=input()
print 'Escribe un valor que no supere' ,(a)
b=input()
while b>a:
    print (b), 'es mayor a' ,(a), 'intentalo otra vez'
    b=input()
li=[b]
a=a-b
while a>0:
    print 'Introduce un valor'
    b=input()
    while b>a:
        print (b), 'es demasiado grande, intentalo otra vez'
        b=input()
    li=li+[b]
    a=a-b
print (li)
    
