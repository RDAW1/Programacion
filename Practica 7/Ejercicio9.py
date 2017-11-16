print 'Introduce una palabra de 3 o mas letras'
a=raw_input()
print 'Introduce otra palabra de 3 o mas letras'
b=raw_input()
def frase(x,y):
    w=0
    for i in range (-1,-4,-1):
        if x[i]==y[i]:
            w=w+1
    if w>=3:
        print 'Las palabras riman'
    elif w==2:
        print 'Las palabras riman un poco'
    else:
        print 'Las palabras no riman'
frase(a,b)
