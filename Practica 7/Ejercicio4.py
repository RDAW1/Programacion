print 'Escribe una frase'
a=raw_input()

def ast(x):
    y=''
    for i in range(len(x)):
        if x[i]==' ':
            y=y+'*'
        else:
            y=y+x[i]
    return y   
print ast(a)
    
