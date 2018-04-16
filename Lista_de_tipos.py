
lista_datos = [3,4,4,"hola",8,"como","estas"]
lista_string = []
lista_numeros = []
for dato in lista_datos:
    if type(dato) == str:
        lista_string.append(dato)
    else:
        lista_numeros.append(dato)

print("la lista de letras es{}".format(lista_string))
print("la lista de numeros es{}".format(lista_numeros))