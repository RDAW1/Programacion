n=int(input('Numero de palabras que tiene la lista: '))
li=[]
for i in range(n):
    print 'Escriba una palabra:'
    p=raw_input()
    li=li+[p]

print 'La lista es: ' ,(li)
li.sort()
print 'La lista ordenada es: ' ,(li)
