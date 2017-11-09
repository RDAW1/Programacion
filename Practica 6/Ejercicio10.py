n=int(raw_input("Numero:"))
d=0
li=[]
for i in range(1,n):
    if n%i==0:
        d=d+i
        li.append(i)
        print li
