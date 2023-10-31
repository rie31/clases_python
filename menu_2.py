fin=False
while fin==False:
    numero_1= input("Por favor ingrese el primer numero: ")
    numero_2= input("Por favor ingrese el segundo numero: ")
    op=input(str("Ingrese una opcion: a) Sumar b) Restar c) Salir: "))
    if (op=="a" or op=="A"):
        print("La suma de ambos numeros es igual a: ", str(int(numero_1)+int(numero_2)))
    elif op== "b" or op== "B":
        print("La resta de ambos numeros es igual a: ", str(int(numero_1)-int(numero_2)))
    elif op=="c" or op=="C":
        fin=True    
print("Hasta luego")