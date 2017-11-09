n=int(input('Numero de palabras que tiene la lista: '))
li=[]
for i in range(n):
    print 'Escriba una palabra:'
    p=raw_input()
    li=li+[p]
print 'La lista es:', li
li2=li
li2.reverse()
print li2
