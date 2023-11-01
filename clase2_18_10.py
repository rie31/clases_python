c=0
while c<=2:
    print("C vale ", c)
    c+=1
else:
    print("Se ha terminado la iteracion, c vale", c)
print("------------------------------ BREAK -----------------------------------------------------")
#BREAK rompe esa condicion
a=0
while a<=5:
    a+=1
    if(a==4):
        print("Rompemos el bucle cuando a vale ", a)
        break
    print("a vale ", a)
else:
    print("Se ha completado la iteracion, a vale ", a)
print("----------------------------- CONTINUE ------------------------------------------------------")
#CONTINUE salta esa condicion
b=0
while(b<=5):
    b+=1
    if(b==3 or b==4):
        continue
    print("b vale ",b)
else:
    print("Iteracion completa, b vale ",b)

print("--------------------  FOR  ---------------------------------------")
#FOR
numeros=[1,2,3,4,5] 
for numero in numeros:
    print(numero)
print("--------------------  FOR EJEMPLO  ---------------------------------------")
for numero in numeros:
    numero*=2
    print(numero)
print("----------------------- ENUMERATE -------------------------")
#ENUMERATE

numeros_2=[1,2,3]
for indice, numero in enumerate(numeros_2):
    numeros_2[indice]*=10
    print(numeros_2)
print("-------------------------- FOR CADENA EJEMPLO 1----------------------")
cadena="Hola chicos UNAHUR"
for caracter in cadena:
    print(caracter)
print("------------------------------- FOR CADENA EJEMPLO 2------------------------------------------")
cadena2="Hola"
cadena3=""
for caracter in cadena2:
    cadena3+=caracter*3
print(cadena3)
print("----------------------------- RANGE ---------------------------------")
#RANGE genera una lista de n° para recorrer pero no ocupa espacio en la memoria
for item in range(10):
    print(item)