
numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 4:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("!Numero añadido¡")

numero_grande = numeros_usuario[0]

suma_de_numeros = numeros_usuario[0] +numeros_usuario[1] +numeros_usuario[2] +numeros_usuario[3]

divisor = len(numeros_usuario)

resultado = suma_de_numeros / divisor

print("El numero mas pequeño es {}".format(resultado))
