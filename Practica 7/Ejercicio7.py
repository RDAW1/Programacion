print 'Introduce una frase'
a=raw_input()
def contar(x):
    w=0
    voc='aeiou'
    for i in range (len(voc)):
        if voc[i] in x:
            w=x.count(voc[i])
        print 'La vocal',voc[i],'aparece',w,'veces.'
contar(a)
