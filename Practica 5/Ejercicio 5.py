print 'Escribe un numero'
a=input()
li=[a]
print 'Escribe un numero mayor que' ,(a)
b=input()
li=li+[b]
while b>a:
    a=b
    print 'Escribe un numero mayor que' ,(a)
    b=input()
    li=li+[b]
li.pop()
print 'Los numeros que has escrito son' ,(li)
    
