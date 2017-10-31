print 'Escribe un numero'
a=input()
li=[a]
print 'Escribe otro numero mayor que' ,(a)
b=input()
while b<=a:
    print (b), 'no es mayor que' ,(a)
    b=input()
li=li+[b]
print 'Los numeros que has escrito son' ,(li)
    
