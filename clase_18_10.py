#Controladores de flujo
a=5
if a==5:
    print("a vale 5")
if a==2:
    print("A vale 2")
print("--------------------------------------------------------------------------------------")
#IF ELIF ELSE

nota= float(input("Introduce una nota: "))
if nota>=9:
    print("La rompiste")
elif nota>=7:
    print("Buen trabajo")
elif nota>=6:
    print("Esta bien..")
elif nota>=5:
    print("Suficiente")
else:
    print("Desaprobaste")
print("--------------------------------------------------------------------------------------")
#ITERACIONES
#WHILE #BREAK
b=0
while b<=5:
    b+=1
    print("b vale ", b)
print("--------------------------------------------------------------------------------------")
d=0
while d<=5:
    d+=1
    if(d==4):
        print("Rompemos el bucle cuando d vale: ", d)
        break
    print("d vale: ", d)
else:
    print("Ha finalizado la iteracion y el valor de d es: ",d)
print("--------------------------------------------------------------------------------------")
e=0
while e<=5:
    e+=1
    if e==3 or e==4:
        continue
    print("e vale: ",e)
else:
    print("Iteracion terminada e vale ",e)
    
