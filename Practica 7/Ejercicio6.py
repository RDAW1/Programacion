print 'Escribe tu nombre'
a=raw_input()
print 'Escribe una letra'
b=raw_input()

def comp(x,y):
    w=0
    w=x.count(y)
    if w>0:
        return 'La letra esta en el nombre'
    else:
        return 'La letra no esta en el nombre'

print comp(a,b)

    
