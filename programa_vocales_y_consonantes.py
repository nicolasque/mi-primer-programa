

frase_Del_usuario = input("introduce una frase aqui:")

vocales = ["a","e","i","o","u"]
n_vocales = 0

no_consonates = [" ","(",")",".",","]
n_consonates = 0

espacios = [" "]
n_espacios = 0

puntos = ["."]
n_puntos = 0

comas = [","]
n_comas = 0

mallusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
n_mallusculas = 0

a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
for letra in frase_Del_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonates += 1
    if letra in no_consonates:
        n_consonates -= 1
    if letra in espacios:
        n_espacios += 1
    if letra in puntos:
        n_puntos += 1
    if letra in comas:
        n_comas += 1
    if letra in mallusculas:
        n_mallusculas += 1
print("las vocales son:")
for letra in frase_Del_usuario:
    if letra in a:
        print(a)
    if letra in e:
        print(e)
    if letra in i:
        print(i)
    if letra in o:
        print(o)
    if letra in u:
        print(u)


print("el numero de vocales son {} y el de consonanates {}".format(n_vocales,n_consonates))
print("el numero de espacios son {}".format(n_espacios))
print("el numero de puntos es {}".format(n_puntos))
print("el numero de comas es {}".format(n_comas))
print("el numero de mallusculas es {}".format(n_mallusculas))