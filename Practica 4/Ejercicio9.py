print 'Escribe el ancho del rectangulo'
a=input()
print 'Escribe alto del rectangulo'
b=input()

for i in range(1):
    for g in range(a):
        print '*',
print

for i in range(b-2):
    for g in range(1):
        print '*',
    for h in range(a-2):
        print ' ',
    for j in range(1):
        print '*',
    print

for i in range(1):
    for g in range(a):
        print '*',
