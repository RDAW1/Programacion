print 'Introduce una frase'
a=raw_input()
def frase(x):
    y=''
    for i in range (len(x)):
        if x[i]==' ':
            y=y
        else:
            y=y+x[i]
    return y
print frase(a)
