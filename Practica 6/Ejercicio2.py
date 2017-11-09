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
    b=raw_input("Escriba la palabra que quiere buscar: ")
    c=0
    for i in li:
        if i==b:
            c=c+1;
    if c==0:
        print 'La palabra' ,(b), 'no aparece en la lista.'
    else:
        print 'La palabra' ,(b), 'aparece' ,(c), 'veces en la lista.'
