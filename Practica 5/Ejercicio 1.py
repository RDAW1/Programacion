print 'Escribe una palabra'
a=raw_input()
li=[a]
while a!='':
    print 'Escribe otra palabra'
    a=raw_input()
    li=li+[a]
li.remove('')
print 'Las palabras que has escrito son' ,(li)
    
