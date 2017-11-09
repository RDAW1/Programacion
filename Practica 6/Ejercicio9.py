n=int(raw_input("Numero de palabras:"))
li=[]
for i in range(1,n+1):
    li.append(raw_input("Palabra:"))
		
print li
li2=[]
for i in li:
    if not i in li2:
        li2.append(i)
li=li2
print li
