print 'Escribe un numero'
a=input()
print 'Escribe otro numero mayor que' ,(a)
b=input()
while b<=a:
    print (b), 'no es mayor que' ,(a)
    print 'Prueba otra vez'
    b=input()
print 'Escribe un numero entre' ,(a), 'y' ,(b)
c=input()
li=[c]
while c>a and c<b:
    print 'Escribe otro numero entre' ,(a), 'y' ,(b)
    c=input()
    li=li+[c]
li.pop()
print 'Los numeros situados entre' ,(a), 'y',(b),'que has escrito son' ,(li)
    
