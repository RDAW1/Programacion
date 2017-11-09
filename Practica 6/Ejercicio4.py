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

e=raw_input('Palabra a eliminar: ')
    for i in range(len(li)-1,-1,-1):
        if li[i]==e:
            del(li[i])
    print 'La lista es ahora:' ,li
