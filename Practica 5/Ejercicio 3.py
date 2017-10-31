print 'Escribe una nota'
a=float(input())
li=[a]
while a>=0 and a<=10:
    print 'Introduce otra nota'
    a=float(input())
    li=li+[a]
li.remove (a)
print 'Las notas que has escrito son' ,(li)
    
