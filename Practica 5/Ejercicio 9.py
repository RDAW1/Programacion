print 'Introduce el nombre'
a=raw_input()
li=[]
lista=[]
while a!='':
   li.append(a)
   print 'Introduce su numero de telefono'
   b=input()
   li.append(b)
   lista=lista+[li]
   print 'Introduce otro nombre'
   a=raw_input()
   li=[]
print (lista)
