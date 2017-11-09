n=int(input('Numero de palabras que tiene la lista: '))
if n < 1:
    print 'Imposible'
else:
    li=[]
    for i in range(n):
        print 'Escriba una palabra:'
        p=raw_input()
        li=li+[p]
    print 'La lista es:', li
