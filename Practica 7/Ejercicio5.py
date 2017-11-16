print 'Escribe una frase'
a=raw_input()
print 'Escribe una vocal'
b=raw_input()

def cambio (x,y):
    v='aeiou'
    w=''
    for i in range(len(x)):
        if x[i] in v:
            w=w+y
        else:
            w=w+x[i]
    return w

print 'La frase es ahora' ,cambio(a,b)
