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
    b=raw_input('Cambiar la palabra: ')
    s=raw_input('por la palabra: ')
    for i in range(len(li)):
        if li[i]==b:
            li[i]=s
    print 'La lista es ahora:' ,li
