
numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("!Numero añadido¡")

numero_grande = numeros_usuario[0]

for numero in numeros_usuario:
    suma_de_numero = numero+numero

divisor = int(len(numeros_usuario))


print("El numero mas pequeño es {}".format(suma_de_numero/divisor))
