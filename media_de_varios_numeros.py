
numeros_usuario = [1]
numero_del_usuario = ""

while len(numeros_usuario) > 5:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("!Numero añadido¡")

for numero in numeros_usuario:
    suma_de_numeros = numero + numero
dividisor = int(len(numeros_usuario))

print("la media es {}".format(suma_de_numeros/dividisor))