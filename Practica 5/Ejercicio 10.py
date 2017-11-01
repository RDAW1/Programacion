print 'Introduce el nombre'
a=raw_input()
li=[]
lista=[]
while a!='':
   li.append(a)
   print 'Introduce las notas del alumno'
   b=float (input())
   while b<=10 and b>=0:
       li.append(b)
       print 'Introduce otra nota'
       b=float (input())
   lista.append(li)
   print 'Introduce otro nombre'
   a=raw_input()
   li=[]
print (lista)
