n=int(input('Numero de palabras que tiene la lista: '))
if n<1:
    print 'Imposible'
else:
    li=[]
    for i in range(n):
        print 'Escriba una palabra:'
        p=raw_input()
        li=li+[p]
    print 'La lista es:', li

m=int(input('Escribe el numero de palabras que quieres eliminar de la lista anterior: '))
if m<1:
    print 'Imposible'
else:
    li2=[]
    for i in range(m):
        print 'Escriba una palabra:'
        p=raw_input()
        li2=li2+[p]
    print 'La lista de palabras a eliminar es:', li2

    for i in li2:
        for j in range(len(li)-1,-1,-1):
            if li[j]==i:
                del(li[j])
    print 'La lista es ahora:' ,li
