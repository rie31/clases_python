#FUNCIONES
def saludar():
    print("Hola")
saludar()
print("___________________________ SCOPE ___________________________________")
def test():
    a=10        #Esta variable existe SOLO dentro de la funcion
    print(a)
a=100
test()
print(a)
print("_____________________________ RETURN ____________________________")
def test():
    return[123,456,7890]
print(test())
print("__________________ RETURN EJEMPLO SUMA ________________________________")
def suma(a,b):
    return a+b
resultado= suma(10,50)
print(resultado)